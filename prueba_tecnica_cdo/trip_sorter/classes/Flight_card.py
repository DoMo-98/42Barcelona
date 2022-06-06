# -*- coding: utf-8 -*-

from classes.Boarding_card import Boarding_card

class Flight_card( Boarding_card ):
    def __init__( self, source, destination, way, seat, gate, baggage="" ):
        super().__init__( source, destination, way, seat )
        self.gate = gate
        self.baggage = baggage
        
    def print_info( self ):
        str = f"From { self.source }, take { self.way } to { self.destination }. Gate { self.gate }, seat { self.seat }. "
        str += f"Baggage { 'will we automatically transferred from your last leg' if not self.baggage else f'drop at { self.baggage }' }."
        print( str )