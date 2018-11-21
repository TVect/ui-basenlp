from rasa_core.policies import Policy, MemoizationPolicy
from rasa_core.events import BotUttered, UserUttered

class RulePolicy(Policy):

    def __init__(self):
        pass

    def train(self,
              training_trackers,  # type: List[DialogueStateTracker]
              domain,  # type: Domain
              **kwargs  # type: **Any
              ):
        # type: (...) -> None
        """Trains the policy on given training trackers."""
        
        pass


    def continue_training(self, training_trackers, domain, **kwargs):
        # type: (List[DialogueStateTracker], Domain, **Any) -> None
        """Continues training an already trained policy.

        This doesn't need to be supported by every policy. If it is supported,
        the policy can be used for online training and the implementation for
        the continued training should be put into this function."""

        pass


    def predict_action_probabilities(self, tracker, domain):
        # type: (DialogueStateTracker, Domain) -> List[float]
        """Predicts the next action the bot should take
        after seeing the tracker.

        Returns the list of probabilities for the next actions"""
        result = [0.0] * domain.num_actions
        last_event = tracker.events[-1]
        if isinstance(last_event, BotUttered):
            result[domain.action_map.get("action_listen")[0]] = 1.0
        elif isinstance(last_event, UserUttered):
            intent = tracker.latest_message.intent
            if intent["name"] == "greet":
                result[domain.action_map.get("utter_greet")[0]] = intent.get("confidence", 1.0)
        return result


    def persist(self, path):
        # type: (Text) -> None
        """Persists the policy to a storage."""
        pass


    @classmethod
    def load(cls, path):
        # type: (Text) -> Policy
        """Loads a policy from the storage.
            Needs to load its featurizer"""
        pass
