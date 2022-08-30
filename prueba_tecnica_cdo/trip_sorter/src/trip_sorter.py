"""#!/usr/bin/python3"""
# -*- coding: utf-8 -*-

from classes.Boarding_card import Boarding_card
from classes.Flight_card import Flight_card

def sort_and_print_cards( card_src_dict, card_dest_list ):
    next_card = None

    for card in card_src_dict.values():
        if card.get_source() not in card_dest_list:
            next_card = card
            card.print_info()
            break

    while next_card.get_destination() in card_src_dict:
        next_card = card_src_dict[ next_card.get_destination() ]
        next_card.print_info()
    
def parse_card_list( card_list ):
    parsed_src_dict = {}
    parsed_dest_list = []
    
    for card in card_list:
        if "flight" in card[ "way" ]:
            parsed_dest_list.append( card[ "destination" ] )
            parsed_src_dict[ card[ "source" ] ] = \
                Flight_card(    source = card[ "source" ] if "source" in card else "",
                                destination = card[ "destination" ] if "destination" in card else "",
                                way = card[ "way" ] if "way" in card else "",
                                seat = card[ "seat" ] if "seat" in card else "",
                                gate = card[ "gate" ] if "gate" in card else "",
                                baggage = card[ "baggage" ] if "baggage" in card else ""
                            )
        else:
            parsed_dest_list.append( card[ "destination" ] )
            parsed_src_dict[ card[ "source" ] ] = \
                Boarding_card(  source = card[ "source" ] if "source" in card else "",
                                destination = card[ "destination" ] if "destination" in card else "",
                                way = card[ "way" ] if "way" in card else "",
                                seat = card[ "seat" ] if "seat" in card else ""
                            )
    
    return (parsed_src_dict, parsed_dest_list)
    