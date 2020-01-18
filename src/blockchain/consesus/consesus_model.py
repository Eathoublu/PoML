from abc import abstractmethod


class ConsensusModel:

    @abstractmethod
    def handle_block(self, block):
        """
        decide how to handle the block given by other peers
        :param block:
        """
        raise NotImplementedError()

    @abstractmethod
    def make_consensus(self, data):
        """
        this method is used to achieve consensus with other peers
        for the sack of writing data into blockchain
        :param data:
        :return:
        """
        raise NotImplementedError()
