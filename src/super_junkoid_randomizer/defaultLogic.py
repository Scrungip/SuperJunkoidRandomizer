from typing import ClassVar

from .item import items_unpackable
from .logicInterface import LocationLogicType, LogicInterface
from .logic_shortcut import LogicShortcut

(
    MagicBolt, Baseball, Sparksuit, RatCloak, WaveBangle, RatBurst, Feather, PurpleLocket, SanguineFin, BloodGem,
    RatDasher, IceGem, DreamersCrown, StormsGem, Wallkicks, DeathGem, MagicBroom, Heart, LuckyFrog, MagicSoap,
    BigLeagueGlove
) = items_unpackable

canRatBurst = LogicShortcut(lambda loadout: (
        (RatCloak in loadout) and (RatBurst in loadout)
))

canRatDash = LogicShortcut(lambda loadout: (
        (RatCloak in loadout) and (RatDasher in loadout)
))

enterLowerOutskirts = LogicShortcut(lambda loadout: (
        ((RatCloak in loadout) and
         (
                 (Feather in loadout) or
                 (Wallkicks in loadout) or
                 (MagicBroom in loadout)
         )) or
        ((Baseball in loadout) and
         (lowerIceCastle in loadout)
         )
))

exitLowerOutskirts = LogicShortcut(lambda loadout: (
        (canRatBurst in loadout) or
        (
                (Baseball in loadout) and
                ((Wallkicks in loadout) or
                 (MagicBroom in loadout) or
                 ((Feather in loadout) and (IceGem in loadout)))
        )
))

lowerOutskirts = LogicShortcut(lambda loadout: (
    ((enterLowerOutskirts in loadout) and (exitLowerOutskirts in loadout))
))

lowerIceCastle = LogicShortcut(lambda loadout: (
        (MagicBroom in loadout) or
        (
                ((Feather in loadout) or (Wallkicks in loadout)) and (IceGem in loadout)
        )
        or
        (
                (canRatBurst in loadout)
                and
                ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
        )
        or
        (
                ((RatCloak in loadout) and
                 (
                         (Feather in loadout) or
                         (Wallkicks in loadout) or
                         (MagicBroom in loadout)
                 ))
                and
                (exitLowerOutskirts in loadout)
        )
))

accessCrocomire = LogicShortcut(lambda loadout: (
        (lowerIceCastle in loadout) and (canRatBurst in loadout) and (Baseball in loadout) and (IceGem in loadout)
))

killCrocomire = LogicShortcut(lambda loadout: (
        (accessCrocomire in loadout) and (loadout.count(MagicBolt) >= 4)
))

accessJunkraid = LogicShortcut(lambda loadout: (
        (lowerIceCastle in loadout) and (canRatBurst in loadout) and (canRatDash in loadout)
))

killJunkraid = LogicShortcut(lambda loadout: (
        (killCrocomire in loadout) and ((accessJunkraid in loadout) or (enterIdolBlood in loadout)) and
        (loadout.count(Heart) >= 4) and (Sparksuit in loadout)
))

bloodBethel = LogicShortcut(lambda loadout: (
        ((canRatBurst in loadout) or
         (
                 (lowerOutskirts in loadout) and
                 (Baseball in loadout) and ((Wallkicks in loadout) or (MagicBroom in loadout))
         )) and
        ((Feather in loadout) or ((SanguineFin in loadout) and ((Wallkicks in loadout) or MagicBroom in loadout)))
        and
        ((SanguineFin in loadout) or (RatCloak in loadout) or (BloodGem in loadout) or (Sparksuit in loadout))
))

botwoon = LogicShortcut(lambda loadout: (
        (bloodBethel in loadout) and (SanguineFin in loadout) and
        ((Wallkicks in loadout) or (MagicBroom in loadout)) and
        (Baseball in loadout) and (loadout.count(Heart) >= 4)
))

accessJunkgon = LogicShortcut(lambda loadout: (
        (bloodBethel in loadout) and (BloodGem in loadout) and
        ((SanguineFin in loadout) or ((Wallkicks in loadout) or (MagicBroom in loadout)))
))

killJunkgon = LogicShortcut(lambda loadout: (
        (botwoon in loadout) and
        ((accessJunkgon in loadout) or enterIdolIce in loadout) and
        (loadout.count(MagicBolt) >= 4) and (Sparksuit in loadout)
))

enterIdolBlood = LogicShortcut(lambda loadout: (
        (accessJunkgon in loadout) and (Sparksuit in loadout) and (canRatBurst in loadout)
))

enterIdolIce = LogicShortcut(lambda loadout: (
        (accessJunkraid in loadout) and (Sparksuit in loadout) and (canRatBurst in loadout)
))

enterIdol = LogicShortcut(lambda loadout: (
        (enterIdolIce in loadout) or (enterIdolBlood in loadout)
))

sporeSpawn = LogicShortcut(lambda loadout: (
        (enterIdol in loadout) and
        ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
))

junkoon = LogicShortcut(lambda loadout: (
        (sporeSpawn in loadout) and (SanguineFin in loadout) and (RatDasher in loadout) and (Sparksuit in loadout)
        and (loadout.count(Heart) >= 8)
))

deepPurple = LogicShortcut(lambda loadout: (
        ((lowerOutskirts in loadout) and (Baseball in loadout)) or
        ((lowerIceCastle in loadout) and (Baseball in loadout)) or
        ((bloodBethel in loadout) and (Baseball in loadout))
))

crateria = LogicShortcut(lambda loadout: (
        (deepPurple in loadout) and (Sparksuit in loadout)
))

junkly = LogicShortcut(lambda loadout: (
        (crateria in loadout) and (canRatBurst in loadout) and
        (((Feather in loadout) and Wallkicks in loadout) or (MagicBroom in loadout)) and
        (PurpleLocket in loadout) and
        (loadout.count(Heart) >= 12) and (loadout.count(MagicBolt) >= 9) and (loadout.count(Baseball) >= 5)
))

location_logic: LocationLogicType = {
    "Outskirts - Hidden Rat Tunnel Magic Bolt": lambda loadout: (
            (RatCloak in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Outskirts - Hidden Pipe Heart": lambda loadout: (
        True
    ),
    "Outskirts - Underwater Pipe Maze Heart": lambda loadout: (
            (MagicBroom in loadout) or
            (((RatCloak in loadout) or Sparksuit in loadout) and
             ((Feather in loadout) or (Wallkicks in loadout))) or
            ((Wallkicks in loadout) and (SanguineFin in loadout))
    ),
    "Lower Outskirts - Ceiling Baseball": lambda loadout: (
            (lowerOutskirts in loadout) and
            ((Wallkicks in loadout) or (MagicBroom in loadout)) and
            (
                    (((BloodGem in loadout) or (IceGem in loadout)) and (RatCloak in loadout))
                    or
                    ((BloodGem in loadout) and (IceGem in loadout))
            )
    ),
    "Lower Outskirts - Wallkick Climb Magic Bolt": lambda loadout: (
            (lowerOutskirts in loadout) and
            ((Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Outskirts - Baseball Alter": lambda loadout: (
            (Baseball in loadout) and (RatCloak in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Outskirts - Hidden Cave Heart": lambda loadout: (
            (RatCloak in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Outskirts - Spider's Magic Bolt": lambda loadout: (
            (Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout)
    ),
    "Outskirts - Hidden Underwater Heart": lambda loadout: (
            (Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout)
    ),
    "Outskirts - Feather": lambda loadout: (
            (Feather in loadout) or
            ((SanguineFin in loadout) and ((Wallkicks in loadout) or (MagicBroom in loadout)))
    ),
    "Outskirts - Rat Cloak": lambda loadout: (
            (Wallkicks in loadout) or (MagicBroom in loadout) or
            ((RatCloak in loadout) and (Feather in loadout))
    ),
    "Lower Outskirts - Rat Burst": lambda loadout: (
            (lowerOutskirts in loadout) and
            ((canRatBurst in loadout) or ((Wallkicks in loadout) and (RatCloak in loadout)))
    ),
    "Lower Outskirts - False Idol Entrance Sparksuit": lambda loadout: (
            (lowerOutskirts in loadout) and
            (Sparksuit in loadout)
    ),
    "Lower Outskirts - Wallkicks": lambda loadout: (
            (lowerOutskirts in loadout) and
            ((Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "False Idol - Left Shaft Heart": lambda loadout: (
            (enterIdol in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "False Idol - Right Shaft Heart": lambda loadout: (
            (enterIdol in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Deep Purple - Wave Bangle": lambda loadout: (  # Deep Purple
            (deepPurple in loadout) and (RatCloak in loadout)
    ),
    "False Idol - Left Hall Magic Bolt": lambda loadout: (
            (enterIdol in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "False Idol - Hidden Shaft Heart": lambda loadout: (
            (sporeSpawn in loadout) and
            ((RatDasher in loadout) or (Sparksuit in loadout)) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "False Idol - Ceiling Crevice Magic Bolt": lambda loadout: (
            (sporeSpawn in loadout) and
            (((Feather in loadout) and (Wallkicks in loadout)) or (MagicBroom in loadout))
    ),
    "False Idol - Under Alter Magic Bolt": lambda loadout: (
        (sporeSpawn in loadout)
    ),
    "False Idol - Dead End Sparksuit": lambda loadout: (
            (sporeSpawn in loadout) and (Sparksuit in loadout)
    ),
    "False Idol - Baseball Alter": lambda loadout: (
        (sporeSpawn in loadout)
    ),
    "False Idol - Spike Spark Heart": lambda loadout: (
            (sporeSpawn in loadout) and (SanguineFin in loadout) and (RatDasher in loadout) and (Sparksuit in loadout)
    ),
    "False Idol - Defiled Junko's Lucky Frog": lambda loadout: (
        (junkoon in loadout)
    ),
    "False Idol - Purple Locket": lambda loadout: (
            (sporeSpawn in loadout) and (SanguineFin in loadout) and (RatDasher in loadout) and (Sparksuit in loadout)
    ),
    "False Idol - Idol's Heart Baseball": lambda loadout: (
        (sporeSpawn in loadout)
    ),
    "Deep Purple - Lavafall Baseball": lambda loadout: (  # Start of Deep Purple
            (deepPurple in loadout) and (canRatBurst in loadout) and (Sparksuit in loadout) and
            ((Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Deep Purple - Big League Glove": lambda loadout: (
            (crateria in loadout) and (canRatBurst in loadout) and (Feather in loadout)
    ),
    "Deep Purple - Toxic Heart": lambda loadout: (
            (crateria in loadout) and (RatCloak in loadout) and
            ((MagicBroom in loadout) or ((Feather in loadout) and (IceGem in loadout)))
    ),
    "Deep Purple - Mother Brain Sparksuit": lambda loadout: (
            ((canRatBurst in loadout) and (Wallkicks in loadout) and (Feather in loadout)) or
            ((crateria in loadout) and (canRatBurst in loadout))
    ),
    "Deep Purple - Under Stairs Magic Bolt": lambda loadout: (
            (crateria in loadout) and (canRatBurst in loadout) and
            (((Feather in loadout) and Wallkicks in loadout) or (MagicBroom in loadout)) and
            (PurpleLocket in loadout)
    ),
    "Deep Purple - Bloodbath Climb Heart": lambda loadout: (
            (crateria in loadout) and (canRatBurst in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Deep Purple - Dashingly Ratty Magic Bolt": lambda loadout: (
            (crateria in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
            and (SanguineFin in loadout) and (canRatDash in loadout)
    ),
    "Deep Purple - Dreamy Crateria Map Station Heart": lambda loadout: (
            (crateria in loadout) and (RatCloak in loadout) and
            ((Feather in loadout) or (SanguineFin in loadout))
    ),
    "Deep Purple - Dreamy Crateria Power Bomb Heart": lambda loadout: (
            (crateria in loadout) and
            (canRatBurst in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Deep Purple - Gem of Storms": lambda loadout: (
            (crateria in loadout) and (canRatBurst in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout)) and
            (StormsGem in loadout) and
            (loadout.count(Heart) >= 8) and (loadout.count(Heart) >= 5)
    ),
    "Deep Purple - Magic Broom": lambda loadout: (
            (crateria in loadout) and (canRatBurst in loadout) and
            (loadout.count(Heart) >= 8) and (loadout.count(MagicBolt) >= 5)
    ),
    "Deep Purple - Baseball Alter": lambda loadout: (
            (crateria in loadout) and (canRatBurst in loadout) and
            (((Feather in loadout) and Wallkicks in loadout) or (MagicBroom in loadout)) and
            (PurpleLocket in loadout)
    ),
    "Deep Purple - Lavabed Magic Bolt": lambda loadout: (
            (crateria in loadout) and (canRatBurst in loadout) and
            (((Feather in loadout) and Wallkicks in loadout) or (MagicBroom in loadout)) and
            (PurpleLocket in loadout)
    ),
    "Deep Purple - Profane Junko's Lucky Frog": lambda loadout: (
        (junkly in loadout)
    ),
    "Ice Castle - Behind Throne Heart": lambda loadout: (  # Start Of Ice Castle
            (
                    (((Feather in loadout) or (Wallkicks in loadout)) and (IceGem in loadout)) or
                    (MagicBroom in loadout)
            ) and
            (RatCloak in loadout)
    ),
    "Ice Castle - Hidden Cave Heart": lambda loadout: (
            (
                    (canRatBurst in loadout) and
                    ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
            ) or
            (
                    (canRatDash in loadout) and
                    (
                            (((Feather in loadout) or (Wallkicks in loadout)) and (IceGem in loadout)) or
                            (MagicBroom in loadout)
                    )
            )

    ),
    "Ice Castle - Freeze Boost Heart": lambda loadout: (
            ((canRatBurst in loadout) and (canRatDash in loadout) and (IceGem in loadout)) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Ice Castle - Spike Jump Magic Bolt": lambda loadout: (
            ((canRatBurst in loadout) and (
                    (Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))) or
            ((((Feather in loadout) or (Wallkicks in loadout)) and (IceGem in loadout)) or
             (MagicBroom in loadout)) or (lowerOutskirts in loadout)
    ),
    "Ice Castle - Dreamer's Shaft Magic Bolt": lambda loadout: (
            (Baseball in loadout) and
            (lowerIceCastle in loadout) and
            (RatCloak in loadout) and
            (((Sparksuit in loadout) and (canRatBurst in loadout)) or (
                    (IceGem in loadout) and (Feather in loadout)) or (MagicBroom in loadout))
    ),
    "Ice Castle - Crystal Cave Sparksuit": lambda loadout: (
            (Sparksuit in loadout) and
            (lowerIceCastle in loadout) and
            (RatCloak in loadout) and
            (Feather in loadout)
    ),
    "Ice Castle - Frozen Speedway Cave Baseball": lambda loadout: (
            (lowerIceCastle in loadout) and (RatCloak in loadout) and
            (
                    (canRatBurst in loadout) or
                    (canRatDash in loadout) and (BloodGem in loadout)
            ) and
            (((Feather in loadout) and (IceGem in loadout)) or (MagicBroom in loadout))
    ),
    "Ice Castle - Bleeder's Cave Magic Bolt": lambda loadout: (
            (lowerIceCastle in loadout) and (RatCloak in loadout) and
            (
                    (canRatBurst in loadout) or
                    (canRatDash in loadout) and (BloodGem in loadout)
            ) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout)) and (SanguineFin in loadout)
    ),
    "Ice Castle - Snowmen's Heart": lambda loadout: (
        (lowerIceCastle in loadout)
    ),
    "Ice Castle - Rat Dasher": lambda loadout: (
            (((Feather in loadout) and (IceGem in loadout)) or
             (MagicBroom in loadout)) and (canRatDash in loadout)
    ),
    "Ice Castle - Gem of Ice": lambda loadout: (
            (killCrocomire in loadout) and (IceGem in loadout)
    ),
    "Ice Castle - Dreamer's Crown": lambda loadout: (
            (lowerIceCastle in loadout) and (Baseball in loadout) and (Sparksuit in loadout) and
            (canRatBurst in loadout) and (loadout.count(Heart) >= 5)
    ),
    "Ice Castle - Baseball Alter": lambda loadout: (
            (lowerIceCastle in loadout) and (Baseball in loadout)
    ),
    "Ice Castle - Immodest Junko's Lucky Frog": lambda loadout: (
        (killJunkraid in loadout)
    ),
    "Blood Bethel - Under Corpses Heart": lambda loadout: (  # Start Of Blood Bethel
            (bloodBethel in loadout) and (canRatBurst in loadout)
    ),
    "Blood Bethel - False Wall Magic Bolt": lambda loadout: (
        (bloodBethel in loadout)
    ),
    "Blood Bethel - Shaft Heart": lambda loadout: (
        (bloodBethel in loadout)
    ),
    "Blood Bethel - Magic Soap": lambda loadout: (
            (bloodBethel in loadout) and (canRatBurst in loadout) and
            ((Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Blood Bethel - Rock Bottom Magic Bolt": lambda loadout: (
        (bloodBethel in loadout)
    ),
    "Blood Bethel - Bloody Barrier's Baseball": lambda loadout: (
            (bloodBethel in loadout) and (BloodGem in loadout) and (canRatBurst in loadout)
    ),
    "Blood Bethel - Speedster Cave Magic Bolt": lambda loadout: (
            (bloodBethel in loadout) and
            ((canRatDash in loadout) or (Sparksuit in loadout))
    ),
    "Blood Bethel - Gem of Blood": lambda loadout: (
            (botwoon in loadout) and (BloodGem in loadout)
    ),
    "Blood Bethel - Hidden Air Pocket Sparksuit": lambda loadout: (
            (bloodBethel in loadout) and (Sparksuit in loadout)
    ),
    "Blood Bethel - Hidden Table Heart": lambda loadout: (
            (bloodBethel in loadout) and
            (
                    ((SanguineFin in loadout) and ((Wallkicks in loadout) or (MagicBroom in loadout))) or
                    (Sparksuit in loadout)
            ) and
            (Baseball in loadout) and (RatCloak in loadout)
    ),
    "Blood Bethel - Sanguine Fin": lambda loadout: (
        (bloodBethel in loadout)
    ),
    "Blood Bethel - Oatsngoats Heart": lambda loadout: (
            ((bloodBethel in loadout) and (BloodGem in loadout) and
             ((SanguineFin in loadout) or ((Wallkicks in loadout) or (MagicBroom in loadout)))) or
            (enterIdolIce in loadout)
    ),
    "Blood Bethel - Baseball Alter": lambda loadout: (
            (bloodBethel in loadout) and (Baseball in loadout)
    ),
    "Blood Bethel - Obscene Junko's Lucky Frog": lambda loadout: (
        (killJunkgon in loadout)
    ),
    "Sheol - Gem of Death": lambda loadout: (  # SHEOL
            (killJunkraid in loadout) and (killJunkgon in loadout) and (junkoon in loadout) and (junkly in loadout) and
            (loadout.count(MagicBolt) >= 15)
    )
}


class Default(LogicInterface):
    location_logic: ClassVar[LocationLogicType] = location_logic
