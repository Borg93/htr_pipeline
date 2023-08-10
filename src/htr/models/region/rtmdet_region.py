from htr.models.base_model import RegionModel


class RtmDetRegionConfig:
    # Define your configuration fields here.
    pass


class RtmDetRegion(RegionModel):
    def __init__(self, config: RtmDetRegionConfig):
        super().__init__(config)

    def preprocess(self, input):
        # Implement preprocessing specific to ModelA
        pass

    def postprocess(self, raw_output):
        # Implement postprocessing specific to ModelA
        pass

    def predict(self, input):
        # Implement prediction logic specific to ModelA
        print("Model region predict")
        return "prediction from rmtdet_region"

    def load_model(self, folder_path):
        # model_file_path = os.path.join(folder_path, 'model.pth')
        # self.model = torch.load(model_file_path)

        print(f"Model loaded: {self.name} from 'model_file_path'")
