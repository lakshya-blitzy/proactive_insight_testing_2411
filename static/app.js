document.getElementById("load").addEventListener("click", async () => {
  const output = document.getElementById("output");
  output.textContent = "Loading...";
  try {
    const response = await fetch("/products");
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    output.textContent = JSON.stringify(await response.json(), null, 2);
  } catch (error) { output.textContent = `Unable to load products: ${error.message}`; }
});
