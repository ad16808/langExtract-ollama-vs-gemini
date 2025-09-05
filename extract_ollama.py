import langextract as lx
import textwrap
import time

start_time = time.time()
# 1. Define the prompt and extraction rules
prompt = textwrap.dedent("""\
    Extract characters, emotions, and relationships in order of appearance.
    Use exact text for extractions. Do not paraphrase or overlap entities.
    Provide meaningful attributes for each entity to add context.""")

# 2. Provide a high-quality example to guide the model
examples = [
    lx.data.ExampleData(
        text="ROMEO. But soft! What light through yonder window breaks? It is the east, and Juliet is the sun.",
        extractions=[
            lx.data.Extraction(
                extraction_class="character",
                extraction_text="ROMEO",
                attributes={"emotional_state": "wonder"}
            ),
            lx.data.Extraction(
                extraction_class="emotion",
                extraction_text="But soft!",
                attributes={"feeling": "gentle awe"}
            ),
            lx.data.Extraction(
                extraction_class="relationship",
                extraction_text="Juliet is the sun",
                attributes={"type": "metaphor"}
            ),
        ]
    )
]

# The input text to be processed
input_text = "Lady Juliet gazed longingly at the stars, her heart aching for Romeo"

# Run the extraction
# Note: Replace "YOUR_API_KEY" with your actual Gemini API key.
result = lx.extract(
    text_or_documents=input_text,
    prompt_description=prompt,
    examples=examples,
    model_id="gemma3:4b",  
    model_url="http://localhost:11434",  # Endpoint URL for self-hosted model. Default Ollama server URL is used here.
    fence_output=False,  # Whether to expect/generate fenced output (```json or ```yaml). When True, model is prompted to generate fenced output and the resolver expects it. When False, raw JSON/YAML is expected.
    use_schema_constraints=False,  # Whether to generate schema constraints for models. LangExtract doesn't implement schema constraints for Ollama models yet
    max_char_buffer=2000,  # Max number of characters for inference
    extraction_passes=2,  # Number of sequential extraction attempts to improve recall and find additional entities. Defaults to 1 (standard single extraction). When > 1, the system performs multiple independent extractions and merges non-overlapping results.
    temperature=0.0
)

# Add code to print the result
for extraction in result.extractions:
    print(f"\nClass: {extraction.extraction_class}")
    print(f"Text: '{extraction.extraction_text}'")
    if extraction.attributes:
        print(f"Attributes: {extraction.attributes}")

print(f"\nTotal extractions found: {len(result.extractions)}")

end_time = time.time()
print(f"\nRunning time: {end_time - start_time:.2f} seconds")