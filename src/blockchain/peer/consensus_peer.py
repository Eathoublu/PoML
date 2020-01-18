class ConsensusPeer:

    def broadcast(self, data):
        self.connector.broadcast(data, self.peer_list)

    def handle_training_request(self, data):
        pass

    def handle_upload_request(self, data):
        self.consensus.make_consensus(data)
