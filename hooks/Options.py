# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################

class StarLvlGoal(Choice):
    """
    Choose your goal.
    """
    display_name = "Star Level Goal"

class PCExclusiveToggle(Toggle):
    """
    Include PC/Switch-exclusive content (Gardens Essences and Commercial Sims).
    If disabled, the exclusive Essences and Sims will be removed from the item pool.
    """
    display_name = "PC/Switch Exclusives"
    default = True

class BFRewardsToggle(Toggle):
    """
    Add Best Friend rewards to the pool, including Commercial Sims'.
    If disabled, Townie Sims will remain in the pool as filler items.
    """
    display_name = "Best Friend Rewards"
    default = True

class UberSimsToggle(Toggle):
    """
    Include Uber Sims' Best Friend rewards.
    If disabled, Uber Sims will remain in the pool as filler items.
    
    NOTE: Enabling this option when best_friend_rewards is disabled will keep Uber Sims rewards in logic.
    """
    display_name = "Uber Sims"
    default = True

class LvlFiveToggle(Toggle):
    """
    Include Level 5 Townie Sims' Best Friend rewards.
    If disabled, the Sims unlocked at level 5 will remain in the pool as filler items.
    
    NOTE: If best_friend_rewards is disabled, Level 5 Sims rewards will be excluded regardless of this option.
    """
    display_name = "Level 5 Sims"
    default = True

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    
    options["goal"] = StarLvlGoal
    options["pc_switch_exclusives"] = PCExclusiveToggle
    options["best_friend_rewards"] = BFRewardsToggle
    options["uber_sims"] = UberSimsToggle
    options["level_5_sims"] = LvlFiveToggle
    
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options
    
    options.type_hints["goal"].aliases.update({"star_level_3":0, "star_level_4":1, "star_level_5":2})
    options.type_hints["goal"].aliases.update({"star_level_3":0, "star_level_4":1, "star_level_5":2})
    options.type_hints["goal"].default = 2

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
