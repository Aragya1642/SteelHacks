import { createRunner } from "@google-labs/breadboard/harness";
import type { Schema } from "@google-labs/breadboard";

// Assume we have a graph that takes text input, processes it,
// and returns a summary.
const config: RunConfig = {
  url: "https://example.com/boards/text-summarizer.bgl.json",
  kits: [
    /* specify kits */
  ],
  // ... more config
};

// Create the runner
const runner = createRunner(config);

// Function to handle user input
async function getUserInput(schema: Schema): Promise<void> {
  // In a real application, this might involve prompting the user through a UI
  console.log("Input required:", schema);
  const input = {
    text: "This is a long piece of text that needs summarizing.",
  };
  await runner.run(input);
}

// Function to handle secret requests
async function getSecret(key: string): Promise<void> {
  // In a real application, this might involve secure storage or user prompts
  console.log("Secret required:", key);
  const secret = "your-api-key-here";
  await runner.run({ [key]: secret });
}

// Set up event listeners
runner.addEventListener("start", (event) => {
  console.log("Runner started:", event.data.timestamp);
});

runner.addEventListener("input", async (event) => {
  if (event.data.inputArguments.schema) {
    await getUserInput(event.data.inputArguments.schema);
  }
});

runner.addEventListener("secret", async (event) => {
  // In real application, there may be more than one secret requested at a
  // time.
  await getSecret(event.data.keys[0]);
});

runner.addEventListener("output", (event) => {
  console.log("Output received:", event.data);
});

runner.addEventListener("nodestart", (event) => {
  console.log("Node started:", event.data.node.id);
});

runner.addEventListener("nodeend", (event) => {
  console.log("Node ended:", event.data.node.id);
});

runner.addEventListener("error", (event) => {
  console.error("An error occurred:", event.data);
});

runner.addEventListener("end", (event) => {
  console.log("Runner finished:", event.data);
});

// Start the runner
runner.run();
