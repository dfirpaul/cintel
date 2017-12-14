import "hash"

rule backdoor_rule
{
	strings:
                $mz = "MZ"
                $pe = "PE" fullword
		$tail = "build-2.2.14"

        condition:
                $mz at 0 and $pe and (filesize == 73802 or $tail) or 
		hash.md5(0, filesize) == "ffa8410d281fbcaeb51430e8bfa04efd"
}

