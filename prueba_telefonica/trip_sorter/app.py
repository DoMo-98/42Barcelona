# -*- coding: utf-8 -*-

from src.trip_sorter import *

def run():
    trip0 = { "source": "Madrid", "destination": "Barcelona", "way": "train 78A", "seat": "45B" }
    trip1 = { "source": "Barcelona", "destination": "Gerona Airport", "way": "airport bus" }
    trip2 = { "source": "Gerona Airport", "destination": "Stockholm", "way": "flight SK455", "gate": "45B", "seat": "3A", "baggage": "ticket counter 344" }
    trip3 = { "source": "Stockholm", "destination": "New York JFK", "way": "flight SK22", "gate": "7B", "seat": "3A" }
    
    card_list = []
    card_list.append( trip2 )
    card_list.append( trip3 )
    card_list.append( trip1 )
    card_list.append( trip0 )
    
    print_cards( sort_cards( parse_card_list( card_list ) ) )
    
    print( "You have arrived at your final destination." )