from abc import abstractmethod


class ConsensusModel:
    @abstractmethod
    def commit_block(self, block):
        """
        decide how to insert the block into the chain
        :param block:
        """
        raise NotImplementedError()

    @abstractmethod
    def handle_block(self, block):
        """
        decide how to handle the block given by other peers
        :param block:
        """
        raise NotImplementedError()


    @abstractmethod
    def verify_block(self, block):
        """
        decide how to verify the block
        :param block:
        """
        raise NotImplementedError()

