#!/usr/bin/perl

$NOHOP = 80  ;#No hop to this point
$EMPTY = 81  ;#Not occupied on board

@BOARD = (($EMPTY) x 63);

sub convertToString($value){

print $value ;
$convertToString = $value;

}

sub displayBoard {
   print "   .0 .1 .2 .3 .4 .5 .6 .7\n";
   foreach $row( 0..7) {
     print "$row   ";
     foreach $col( 0..7 ) {
        #print "$BOARD[$row + $col] ";
        print $convertToString($BOARD[$row + $col]) ;
     }
   print "\n";
   }

}

&displayBoard;
