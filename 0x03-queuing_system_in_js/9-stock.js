const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

const getItemById = (id) => listProducts.find(product => product.itemId === id);

async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock !== null ? parseInt(stock, 10) : null;
}

const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);
  
  if (!product) {
    res.status(404).json({ status: 'Product not found' });
    return;
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const availableQuantity = currentStock !== null ? currentStock : product.initialAvailableQuantity;

  res.json({ 
    itemId: product.itemId, 
    itemName: product.itemName, 
    price: product.price, 
    initialAvailableQuantity: product.initialAvailableQuantity, 
    currentQuantity: availableQuantity 
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);
  
  if (!product) {
    res.status(404).json({ status: 'Product not found' });
    return;
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const availableQuantity = currentStock !== null ? currentStock : product.initialAvailableQuantity;

  if (availableQuantity <= 0) {
    res.json({ status: 'Not enough stock available', itemId });
  } else {
    await reserveStockById(itemId, availableQuantity - 1);
    res.json({ status: 'Reservation confirmed', itemId });
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
