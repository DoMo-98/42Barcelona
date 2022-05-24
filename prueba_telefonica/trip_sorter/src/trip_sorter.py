"""#!/usr/bin/python3"""
# -*- coding: utf-8 -*-

from classes.Boarding_card import Boarding_card
from classes.Flight_card import Flight_card

def print_cards( card_pointer ):
    while card_pointer:
        # card_pointer.print()
        card_pointer.print_info()
        card_pointer = card_pointer.get_next()

def sort_cards( card_list ):
    i = 0
    
    while i < len( card_list ) - 1:
        
        j = i + 1
        while j < len( card_list ):
            
            if card_list[ i ].get_destination() == card_list[ j ].get_source():
                card_list[ i ].set_next( card_list[ j ] )
                card_list[ j ].set_prev( card_list[ i ] )
                
            if card_list[ j ].get_destination() == card_list[ i ].get_source():
                card_list[ j ].set_next( card_list[ i ] )
                card_list[ i ].set_prev( card_list[ j ] )
                
            j += 1
        i += 1
        
    for i in card_list:
        if not i.get_prev():
            return i
    
    return None
    
def parse_card_list( card_list ):
    parsed_card_list = []
    
    for card in card_list:
        if "flight" in card[ "way" ]:
            parsed_card_list.append(
                Flight_card(    source = card[ "source" ] if "source" in card else "",
                                destination = card[ "destination" ] if "destination" in card else "",
                                way = card[ "way" ] if "way" in card else "",
                                seat = card[ "seat" ] if "seat" in card else "",
                                gate = card[ "gate" ] if "gate" in card else "",
                                baggage = card[ "baggage" ] if "baggage" in card else ""
                            )
            )
        else:
            parsed_card_list.append(
                Boarding_card(  source = card[ "source" ] if "source" in card else "",
                                destination = card[ "destination" ] if "destination" in card else "",
                                way = card[ "way" ] if "way" in card else "",
                                seat = card[ "seat" ] if "seat" in card else ""
                            )
            )
    
    return parsed_card_list
    