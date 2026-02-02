class DataLoader:
    def load_csv_to_Database(self,file_path):
        try:
            data = pd.read_csv(file_path, dtype=str)
            return data
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            return None
    def load_json_to_Database(self,file_path):
        try:
            data = pd.read_json(file_path)
            return data
        except Exception as e:
            print(f"Error loading JSON file: {e}")
            return None