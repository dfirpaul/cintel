rule PE_File
{
	strings:
                $mz = "MZ"
                $pe = "PE"

        condition:
                $mz and $pe
}

