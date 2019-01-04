class ExamSetup:
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client

    def execute(self):
        print("Exam setup")
