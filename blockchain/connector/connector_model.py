from abc import abstractmethod


class ConnectorModel:

    @abstractmethod
    def broadcast(self, data, target: list):
        """
        broadcast the data to all peers
        :param data:
        :param target:
        """
        pass

    @abstractmethod
    def handle_customer_request(self):
        pass
