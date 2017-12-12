rule PE_File
{
	strings:
                $mz = "MZ"
                $pe = "PE"

        condition:
                $mz at 5 and $pe
}

