import json

class ListManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self._read_file()
    
    def _read_file(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)
    
    def _write_file(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)
    
    def add_entry(self, url, title, data, abstract):
        # Determina il nuovo ID incrementando di 1 rispetto al più grande esistente
        new_id = str(max(int(item['id']) for item in self.data) + 1)
        new_entry = {
            "id": new_id,
            "url": url,
            "title": title,
            "data": data,
            "abstract": abstract
        }
        # Aggiunge il nuovo elemento all'inizio della lista
        self.data.insert(0, new_entry)
        # Salva il file aggiornato
        self._write_file()