import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

/* =========================
   Data
========================= */

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

/* =========================
   Data access
========================= */

const getItemById = (id) =>
  listProducts.find((item) => item.id === id);

/* =========================
   Redis client
========================= */

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

/* =========================
   Redis helpers
========================= */

const reserveStockById = async (itemId, stock) => {
  await setAsync(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  const stock = await getAsync(`item.${itemId}`);
  return stock === null ? null : Number(stock);
};

/* =========================
   Server
========================= */

const app = express();
const PORT = 1245;

/* =========================
   Routes
========================= */

/**
 * GET /list_products
 */
app.get('/list_products', (req, res) => {
  const products = listProducts.map((item) => ({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
  }));

  res.json(products);
});

/**
 * GET /list_products/:itemId
 */
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  let currentQuantity = await getCurrentReservedStockById(itemId);

  if (currentQuantity === null) {
    currentQuantity = item.stock;
  }

  return res.json({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity,
  });
});

/**
 * GET /reserve_product/:itemId
 */
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  let currentQuantity = await getCurrentReservedStockById(itemId);

  if (currentQuantity === null) {
    currentQuantity = item.stock;
  }

  if (currentQuantity <= 0) {
    return res.json({
      status: 'Not enough stock available',
      itemId,
    });
  }

  await reserveStockById(itemId, currentQuantity - 1);

  return res.json({
    status: 'Reservation confirmed',
    itemId,
  });
});

/* =========================
   Start server
========================= */

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
