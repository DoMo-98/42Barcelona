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