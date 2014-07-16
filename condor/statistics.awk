#
# Berechnet Mittelwert und Standardabweichung fuer allen Spalten in einer Datei
# Kommentarzeilen muessen mit # anfangen
# Nur Zeilen die mit Zahlen anfangen werden beruecksichtigt
#
BEGIN {
	number = 0; sum1 = 0.0; sum2 = 0.0; min = 99999999.0; max = 0.0;
}
/^\#/ {next;}
{
	number = number + 1;
	sum1 = sum1 + $1;
	sum2 = sum2 + $1*$1;
	if ($1 < min)
	{
		min = $1
	}
	if ($1 > max)
	{
		max = $1
	}
}
END {
	if (number > 0) {
	    print "Data points = ", number;
	    print "Mean        = ", sum1/number;
	    print "Minimum     = ", min;
	    print "Maximum     = ", max;
	    print "sigma       = ", sqrt(1.0/number * ( sum2 - (sum1*sum1/number)));
	    print "rms         = ", sqrt(sum2/number);
	}
}
