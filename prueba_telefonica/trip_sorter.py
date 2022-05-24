"""#!/usr/bin/python3"""
# -*- coding: utf-8 -*-

class Boarding_card:
    
    def __init__( self, source, destination, way, seat="" ):
        self.source = source
        self.destination = destination
        self.next = None
        self.prev = None
        self.way = way
        self.seat = seat
    
    def get_next( self ):
        return self.next
        
    def set_next( self, next ):
        self.next = next
        
    def get_prev( self ):
        return self.prev
        
    def set_prev( self, prev ):
        self.prev = prev
    
    def get_source( self ):
        return self.source
    
    def get_destination( self ):
        return self.destination
        
    # def print( self ):
    #     print( f"From {self.source} to {self.destination}" )
    
    def print_info( self ):
        str = f"Take { self.way } from { self.source } to { self.destination }. "
        str += f"{ 'No seat assignment' if not self.seat else f'Sit in seat { self.seat }' }."
        print( str )
        
        
class Flight_card( Boarding_card ):
    def __init__( self, source, destination, way, seat, gate, baggage="" ):
        super().__init__( source, destination, way, seat )
        self.gate = gate
        self.baggage = baggage
        
    def print_info( self ):
        str = f"From { self.source }, take { self.way } to { self.destination }. Gate { self.gate }, seat { self.seat }. "
        str += f"Baggage { 'will we automatically transferred from your last leg' if not self.baggage else f'drop at { self.baggage }' }."
        print( str )


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
    
def main():
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
    
if __name__ == "__main__":
    main()

