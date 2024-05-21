#metro
vc_metro = {
  'Richmond-Brighouse': set(['Lansdowne']),
  'Lansdowne': set(['Richmond-Brighouse', 'Aberdeen']),
  'Aberdeen': set(['Lansdowne', 'Bridgeport']),
  'Bridgeport': set(['Aberdeen', 'Templeton', 'Marine Drive']),
  'YVR-Airport': set(['Sea Island Centre']),
  'Sea Island Centre': set(['YVR-Airport', 'Templeton']),
  'Templeton': set(['Sea Island Centre', 'Bridgeport']),
  'Marine Drive': set(['Bridgeport', 'Langara-49th Avenue']),
  'Langara-49th Avenue': set(['Marine Drive', 'Oakbridge-41st Avenue']),
  'Oakbridge-41st Avenue': set(['Langara-49th Avenue', 'King Edward']),
  'King Edward': set(['Oakbridge-41st Avenue', 'Broadway-City Hall']),
  'Broadway-City Hall': set(['King Edward', 'Olympic Village']),
  'Olympic Village': set(['Broadway-City Hall', 'Yaletown-Roundhouse']),
  'Yaletown-Roundhouse': set(['Olympic Village', 'Vancouver City Centre']),
  'Vancouver City Centre': set(['Yaletown-Roundhouse', 'Waterfront']),
  'Waterfront': set(['Vancouver City Centre', 'Burrard']),
  'Burrard': set(['Waterfront', 'Granville']),
  'Granville': set(['Burrard', 'Stadium-Chinatown']),
  'Stadium-Chinatown': set(['Granville', 'Main Street-Science World']),
  'Main Street-Science World': set(['Stadium-Chinatown', 'Commercial-Broadway']),
  'Commercial-Broadway': set(['VCC-Clark', 'Main Street-Science World', 'Renfrew', 'Nanaimo']),
  'VCC-Clark': set(['Commercial-Broadway']),
  'Nanaimo': set(['Commercial-Broadway', '29th Avenue']),
  '29th Avenue': set(['Nanaimo', 'Joyce-Collingwood']),
  'Joyce-Collingwood': set(['29th Avenue', 'Patterson']),
  'Patterson': set(['Joyce-Collingwood', 'Metrotown']),
  'Metrotown': set(['Patterson', 'Royal Oak']),
  'Royal Oak': set(['Metrotown', 'Edmonds']),
  'Edmonds': set(['Royal Oak', '22nd Street']),
  '22nd Street': set(['Edmonds', 'New Westminster']),
  'New Westminster': set(['22nd Street', 'Columbia']),
  'Columbia': set(['New Westminster', 'Sapperton', 'Scott Road']),
  'Scott Road': set(['Columbia', 'Gateway']),
  'Gateway': set(['Scott Road', 'Surrey Central']),
  'Surrey Central': set(['Gateway', 'King George']),
  'King George': set(['Surrey Central']),
  'Sapperton': set(['Columbia', 'Braid']),
  'Braid': set(['Sapperton', 'Lougheed Town Centre']),
  'Lougheed Town Centre': set(['Braid', 'Production Way / University', 'Burquitlam']),
  'Burquitlam': set(['Lougheed Town Centre', 'Moody Centre']),
  'Moody Centre': set(['Burquitlam', 'Inlet Centre']),
  'Inlet Centre': set(['Moody Centre', 'Coquitlam Central']),
  'Coquitlam Central': set(['Inlet Centre', 'Lincoln']),
  'Lincoln': set(['Coquitlam Central', 'Lafarge Lake-Douglas']),
  'Lafarge Lake-Douglas': set(['Lincoln']),
  'Production Way / University': set(['Lougheed Town Centre', 'Lake City Way']),
  'Lake City Way': set(['Production Way / University', 'Sperling / Burnaby Lake']),
  'Sperling / Burnaby Lake': set(['Lake City Way', 'Holdom']),
  'Holdom': set(['Sperling / Burnaby Lake', 'Brentwood Town Centre']),
  'Brentwood Town Centre': set(['Holdom', 'Gilmore']),
  'Gilmore': set(['Brentwood Town Centre', 'Rupert']),
  'Rupert': set(['Gilmore', 'Renfrew']),
  'Renfrew': set(['Rupert', 'Commercial-Broadway'])
  }