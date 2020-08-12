import re
rr="Department of Computer Science was established in the year 2009 under the Shivaji University Kolhapur with the basic" \
   " intake of 60. It is established with the objective of imparting quality education in the field of Computer Science. " \
   "With rapidly evolving technology and the continuous need for innovation the department has always produced quality " \
   "professionals, holding important positions in Information Technology industry in India and abroad.Our alumni are at " \
   "the forefront of research and development in computer science and related fields within India and internationally." \
   " The department's alumni include renowned academicians, leaders in computer and IT industry, distinguished software " \
   "professionals, and trendsetting entrepreneurs.All graduates of CSE finds excellent placements in top ranking global " \
   "software companies."
patt=re.compile(r"alumni")

matches=patt.finditer(rr)
for match in matches:
   print(match)
