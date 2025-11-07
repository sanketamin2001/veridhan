
# Read all the HTML files to understand the full structure
files_to_read = {
    'index.html': '671250f3-8d58-4b7a-ba3c-bb0675ae863d',
    'about.html': '99aff2ba-fabf-4de6-bfe7-d35ad49e72a1',
    'services.html': '8b023880-e66c-46e1-8491-12cf9e1a3157',
    'contact.html': '7dec74f0-23f8-446e-8248-69d9d51a2e2e',
    'disclaimer.html': 'a605ba3d-482e-4057-ab2e-b7bf45aed253',
    'styles.css': 'b98b612f-6b74-42cf-b277-5b539faf52b5'
}

file_contents = {}
for filename in files_to_read.keys():
    with open(filename, 'r', encoding='utf-8') as f:
        file_contents[filename] = f.read()
        
print("Files loaded successfully:")
for filename in file_contents.keys():
    print(f"  - {filename}: {len(file_contents[filename])} characters")
