import re
import hermes
import json

def stringsearch(z,t):
  if t == "H":
    hazardphraseslist = re.findall(r"H[2-4]\d\d", z)
    results = []
    for i in hazardphraseslist:
      if i not in results:
        results.append(i)
    return
  elif t == "cid":
     match = re.search(r"(\"cid\"\:\s)([0-9]+)", z)
     return match.group(2)
  else:
    pass



newvar = {
  "PC_Substances": [
    {
      "sid": {
        "id": 48420065,
        "version": 2
      },
      "source": {
        "db": {
          "name": "EPA DSSTox",
          "source_id": {
            "str": "29669"
          },
          "date": {
            "std": {
              "year": 2008,
              "month": 2,
              "day": 15
            }
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Nitric acid ammonium salt",
        "ammonium nitrate"
      ],
      "comment": [
        "Substance included in EPA DSSTox HPVCSI: EPA High Production Volume (HPV) Challenge Program Structure-Index File [link to DSSTox SDF Download Page] http://www.epa.gov/ncct/dsstox/sdf_hpvcsi.html",
        "Structure Shown: tested chemical",
        "For further information visit the EPA HPV Challenge Website http://www.epa.gov/chemrtk/"
      ],
      "xref": [
        {
          "regid": "29669"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.epa.gov/ncct/dsstox/sdf_hpvcsi.html"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              1,
              2
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    1.9831,
                    0,
                    2.0111,
                    1.3252,
                    4.6661
                  ],
                  "y": [
                    -2.3004,
                    -1.1012,
                    0,
                    -1.1339,
                    -1.1479
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 48424826,
        "version": 2
      },
      "source": {
        "db": {
          "name": "EPA DSSTox",
          "source_id": {
            "str": "33189"
          },
          "date": {
            "std": {
              "year": 2008,
              "month": 2,
              "day": 15
            }
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium nitrate"
      ],
      "comment": [
        "Substance included in EPA DSSTox NTPHTS: National Toxicology Program (NTP) High Throughput Screening Project Structure-Index File [link to DSSTox SDF Download Page] http://www.epa.gov/ncct/dsstox/sdf_ntphts.html",
        "Structure Shown: tested chemical",
        "For further information visit the National Institute of Environmental Health Sciences (NIEHS) NTP High Throughput Screening Initiative Website http://ntp.niehs.nih.gov/index.cfm?objectid=05F80E15-F1F6-975E-77DDEDBDF3B941CD"
      ],
      "xref": [
        {
          "regid": "33189"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.epa.gov/ncct/dsstox/sdf_ntphts.html"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              1,
              2
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    1.9831,
                    0,
                    2.0111,
                    1.3252,
                    4.6661
                  ],
                  "y": [
                    -2.3004,
                    -1.1012,
                    0,
                    -1.1339,
                    -1.1479
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 49855689,
        "version": 1
      },
      "source": {
        "db": {
          "name": "LeadScope",
          "source_id": {
            "str": "LS-1555"
          }
        }
      },
      "synonyms": [
        "AMMONIUM NITRATE (PESTICIDE/FERTILIZER MIXTURE)",
        "Ammonium nitrate",
        "Ammonium nitrate solution",
        "Ammonium nitrate solution (greater than 45% and less than 93%)",
        "Ammonium nitrate, liquid (hot concentrated solution) [UN2426] [Oxidizer]",
        "Ammonium nitrate, solution",
        "Ammonium nitrate, urea solution (containing ammonia)",
        "Ammonium nitrate, urea solution (not containing ammonia)",
        "Ammonium nitrate, with >0.2% combustible substances, including any organic substance calculated as carbon, to the exclusion of any other added substance [UN0222] [Explosive 1.1D]",
        "Ammonium nitrate, with not >0.2% of combustible substances, including any organic substance calculated as carbon, to the exclusion of any other added substance [UN1942] [Oxidizer]",
        "Ammonium nitricum",
        "Ammonium saltpeter",
        "Ammonium(I) nitrate (1:1)",
        "Caswell No. 045",
        "EINECS 229-347-8",
        "EPA Pesticide Chemical Code 076101",
        "German saltpeter",
        "HSDB 475",
        "Herco prills",
        "LS-1555",
        "Merco Prills",
        "Nitram",
        "Nitrate d'ammonium [French]",
        "Nitrate of ammonia",
        "Nitrato amonico [Spanish]",
        "Nitric acid ammonium salt",
        "Nitric acid, ammonium salt",
        "Norway saltpeter",
        "UN0222",
        "UN1942",
        "UN2426",
        "Varioform I"
      ],
      "xref": [
        {
          "regid": "LS-1555"
        },
        {
          "dburl": "http://www.leadscope.com"
        },
        {
          "sburl": "http://www.leadscope.com/structure_search_results.php?ss_string=LS-1555"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              1,
              2
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    -0.2369,
                    -0.0499,
                    -1.6328,
                    -0.644,
                    2.5634
                  ],
                  "y": [
                    -0.8807,
                    0.8393,
                    0.1704,
                    0.0416,
                    -0.1704
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 56311070,
        "version": 1
      },
      "source": {
        "db": {
          "name": "EPA DSSTox",
          "source_id": {
            "str": "43607"
          },
          "date": {
            "std": {
              "year": 2008,
              "month": 10,
              "day": 21
            }
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium Nitrate"
      ],
      "comment": [
        "Substance included in EPA DSSTox ARYEXP: European Bioinformatics Institute (EBI) ArrayExpress Repository for Gene Expression Experiments Structure-Index Locator File [link to DSSTox SDF Download Page] http://www.epa.gov/ncct/dsstox/sdf_aryexp.html",
        "Structure Shown: tested chemical",
        "For further information visit the ArrayExpress Repository Microarray Experiment Accession ID E-MEXP-573 Display ArrayExpress Webpage http://www.ebi.ac.uk/arrayexpress/experiments/E-MEXP-573"
      ],
      "xref": [
        {
          "regid": "43607"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.epa.gov/ncct/dsstox/sdf_aryexp.html"
        },
        {
          "sburl": "http://www.ebi.ac.uk/arrayexpress/experiments/E-MEXP-573"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              1,
              2
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    1.9831,
                    0,
                    2.0111,
                    1.3252,
                    4.6661
                  ],
                  "y": [
                    -2.3004,
                    -1.1012,
                    0,
                    -1.1339,
                    -1.1479
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 56311379,
        "version": 1
      },
      "source": {
        "db": {
          "name": "EPA DSSTox",
          "source_id": {
            "str": "44063"
          },
          "date": {
            "std": {
              "year": 2008,
              "month": 10,
              "day": 21
            }
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium Nitrate"
      ],
      "comment": [
        "Substance included in EPA DSSTox ARYEXP: European Bioinformatics Institute (EBI) ArrayExpress Repository for Gene Expression Experiments Structure-Index Locator File [link to DSSTox SDF Download Page] http://www.epa.gov/ncct/dsstox/sdf_aryexp.html",
        "Structure Shown: tested chemical",
        "For further information visit the ArrayExpress Repository Microarray Experiment Accession ID E-MEXP-729 Display ArrayExpress Webpage http://www.ebi.ac.uk/arrayexpress/experiments/E-MEXP-729"
      ],
      "xref": [
        {
          "regid": "44063"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.epa.gov/ncct/dsstox/sdf_aryexp.html"
        },
        {
          "sburl": "http://www.ebi.ac.uk/arrayexpress/experiments/E-MEXP-729"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              1,
              2
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    1.9831,
                    0,
                    2.0111,
                    1.3252,
                    4.6661
                  ],
                  "y": [
                    -2.3004,
                    -1.1012,
                    0,
                    -1.1339,
                    -1.1479
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 56314412,
        "version": 1
      },
      "source": {
        "db": {
          "name": "EPA DSSTox",
          "source_id": {
            "str": "49460"
          },
          "date": {
            "std": {
              "year": 2008,
              "month": 10,
              "day": 23
            }
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium nitrate"
      ],
      "comment": [
        "Substance included in EPA DSSTox GEOGSE: National Center for Biotechnology Information (NCBI) Gene Expression Omnibus (GEO) Series Experiment Structure-Index Locator File [link to DSSTox SDF Download Page] http://www.epa.gov/ncct/dsstox/sdf_geogse.html",
        "Structure Shown: tested chemical",
        "For further information visit GEO Series Microarray Experiment Accession ID GSE9258 Display GEO Series Webpage http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE9258target=_blank"
      ],
      "xref": [
        {
          "regid": "49460"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.epa.gov/ncct/dsstox/sdf_geogse.html"
        },
        {
          "sburl": "http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE9258"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              1,
              2
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    1.9831,
                    0,
                    2.0111,
                    1.3252,
                    4.6661
                  ],
                  "y": [
                    -2.3004,
                    -1.1012,
                    0,
                    -1.1339,
                    -1.1479
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 126522801,
        "version": 8
      },
      "source": {
        "db": {
          "name": "ChEBI",
          "source_id": {
            "str": "CHEBI:63038"
          },
          "date": {
            "std": {
              "year": 2020,
              "month": 4,
              "day": 6
            }
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "ammonium nitrate",
        "Ammonium(I) nitrate (1:1)",
        "Nitrate d'ammonium",
        "Nitric acid ammonium salt (1:1)",
        "Nitrate of ammonia",
        "Ammonium nitricum",
        "Ammonium saltpeter",
        "Norway saltpeter",
        "Nitrato amonico",
        "Nitric acid, ammonium salt",
        "CHEBI:63038"
      ],
      "comment": [
        "Being an oxidising agent, ammonium nitrate (AN) is commonly mixed with fuel to make explosives. Under normal conditions, it is quite stable (i.e. it is an ingredient of many explosives, rather than an explosive itself). However, when heated (e.g. in a fire), AN can decompose, producing oxygen and a lot of heat. The heat produced causes more AN to decompose, generating more heat, and so on, while the oxygen produced causes the fire to burn more vigorously. The result is that once started, the thermal decomposition is generally impossible to stop and will often end in an explosion - see, for example, http://en.wikipedia.org/wiki/Texas_City_Disaster"
      ],
      "xref": [
        {
          "dburl": "http://www.ebi.ac.uk/chebi/"
        },
        {
          "sburl": "http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:63038"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "regid": "CHEBI:63038"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              7,
              8,
              8,
              8,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": 1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 3,
                "value": -1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              1,
              4
            ],
            "aid2": [
              2,
              3,
              1
            ],
            "order": [
              1,
              1,
              2
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    5.5455,
                    6.26,
                    4.831,
                    5.5455,
                    5.3711
                  ],
                  "y": [
                    -12.449,
                    -12.8615,
                    -12.8615,
                    -11.624,
                    -13.5394
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 134988773,
        "version": 8
      },
      "source": {
        "db": {
          "name": "ChemIDplus",
          "source_id": {
            "str": "0006484522"
          }
        }
      },
      "synonyms": [
        "T8YA51M7Y6",
        "6484-52-2",
        "Ammonium nitrate",
        "Ammonium(I) nitrate (1:1)",
        "Nitric acid ammonium salt (1:1)",
        "Nitric acid ammonium salt",
        "Ammonium saltpeter",
        "Caswell No. 045",
        "EINECS 229-347-8",
        "EPA Pesticide Chemical Code 076101",
        "German saltpeter",
        "Herco prills",
        "HSDB 475",
        "Merco Prills",
        "Nitram",
        "Nitrate d'ammonium [French]",
        "Nitrate of ammonia",
        "Nitrato amonico [Spanish]",
        "Nitric acid, ammonium salt",
        "Norway saltpeter",
        "Varioform I",
        "Ammonium nitricum",
        "Nitrate d'ammonium",
        "Nitrato amonico",
        "UNII-T8YA51M7Y6",
        "EC 229-347-8",
        "Ammonium nitrate, liquid (hot concentrated solution) [UN2426]  [Oxidizer]",
        "Ammonium nitrate solution",
        "Ammonium nitrate, solution",
        "Ammonium nitrate solution (greater than 45% and less than 93%)",
        "Ammonium nitrate, urea solution (containing ammonia)",
        "Ammonium nitrate, urea solution (not containing ammonia)",
        "Ammonium nitrate, with >0.2% combustible substances, including any organic substance calculated as carbon, to the exclusion of any other added substance [UN0222]  [Explosive 1.1D]",
        "Ammonium nitrate, with not >0.2% of combustible substances, including any organic substance calculated as carbon, to the exclusion of any other added substance [UN1942]  [Oxidizer]",
        "UN0222",
        "UN1942",
        "UN2426",
        "Ammonium nitrate, with >0.2% combustible substances, including any organic substance calculated as carbon, to the exclusion of any other added substance",
        "Ammonium nitrate, with not >0.2% of combustible substances, including any organic substance calculated as carbon, to the exclusion of any other added substance",
        "Ammonium nitrate, liquid (hot concentrated solution)"
      ],
      "comment": [
        "Fertilizers",
        "[Other Registry Number] 893438-76-1",
        "[Other Registry Number] 95255-40-6",
        "Agrochemicals",
        "[Other Registry Number] 1388628-04-3",
        "Explosive Agents",
        "T8YA51M7Y6",
        "0006484522"
      ],
      "xref": [
        {
          "dburl": "https://chem.nlm.nih.gov/chemidplus/"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "sburl": "https://chem.nlm.nih.gov/chemidplus/id/0006484522"
        },
        {
          "regid": "0006484522"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              7,
              8,
              8,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": 1
              },
              {
                "aid": 3,
                "value": -1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              2,
              2,
              2
            ],
            "aid2": [
              1,
              3,
              4
            ],
            "order": [
              1,
              1,
              2
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    4.846,
                    4.131,
                    3.4176,
                    4.1309,
                    2.0783
                  ],
                  "y": [
                    -4.2584,
                    -3.8456,
                    -4.26,
                    -3.0245,
                    -4.2489
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 144204728,
        "version": 3
      },
      "source": {
        "db": {
          "name": "824",
          "source_id": {
            "str": "NCGC00091921-01"
          }
        }
      },
      "synonyms": [
        "Ammonium nitrate",
        "CAS-6484-52-2",
        "DSSTox_CID_9668",
        "DSSTox_GSID_29668",
        "DSSTox_RID_78802",
        "NCGC00091921-01",
        "Tox21_111177"
      ],
      "comment": [
        "TOX21S_v5a"
      ],
      "xref": [
        {
          "regid": "NCGC00091921-01"
        },
        {
          "dburl": "https://tripod.nih.gov/tox21"
        },
        {
          "sburl": "https://tripod.nih.gov/tox21/samples/Tox21_111177"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              1,
              2
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    1.2342,
                    0,
                    1.2516,
                    0.8247,
                    2.904
                  ],
                  "y": [
                    -1.4317,
                    -0.6853,
                    0,
                    -0.7057,
                    -0.7144
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 144209469,
        "version": 3
      },
      "source": {
        "db": {
          "name": "824",
          "source_id": {
            "str": "NCGC00259820-01"
          }
        }
      },
      "synonyms": [
        "Ammonium nitrate",
        "CAS-6484-52-2",
        "DSSTox_CID_9668",
        "DSSTox_GSID_29668",
        "DSSTox_RID_78802",
        "NCGC00259820-01",
        "Tox21_202271"
      ],
      "comment": [
        "TOX21S_v5a"
      ],
      "xref": [
        {
          "regid": "NCGC00259820-01"
        },
        {
          "dburl": "https://tripod.nih.gov/tox21"
        },
        {
          "sburl": "https://tripod.nih.gov/tox21/samples/Tox21_202271"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              1,
              2
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    1.2342,
                    0,
                    1.2516,
                    0.8247,
                    2.904
                  ],
                  "y": [
                    -1.4317,
                    -0.6853,
                    0,
                    -0.7057,
                    -0.7144
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 144213829,
        "version": 3
      },
      "source": {
        "db": {
          "name": "824",
          "source_id": {
            "str": "NCGC00257475-01"
          }
        }
      },
      "synonyms": [
        "Ammonium nitrate",
        "CAS-6484-52-2",
        "DSSTox_CID_9668",
        "DSSTox_GSID_29668",
        "DSSTox_RID_78802",
        "NCGC00257475-01",
        "Tox21_303522"
      ],
      "comment": [
        "TOX21S_v5a"
      ],
      "xref": [
        {
          "regid": "NCGC00257475-01"
        },
        {
          "dburl": "https://tripod.nih.gov/tox21"
        },
        {
          "sburl": "https://tripod.nih.gov/tox21/samples/Tox21_303522"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              1,
              2
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    1.2342,
                    0,
                    1.2516,
                    0.8247,
                    2.904
                  ],
                  "y": [
                    -1.4317,
                    -0.6853,
                    0,
                    -0.7057,
                    -0.7144
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 162092564,
        "version": 1
      },
      "source": {
        "db": {
          "name": "1052",
          "source_id": {
            "str": "105723"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "ammonium nitrate",
        "ammonium nitronate"
      ],
      "xref": [
        {
          "regid": "105723"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.chembase.cn"
        },
        {
          "sburl": "http://www.chembase.cn/molecule-105723.html"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              1,
              2
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    3.2411,
                    3.2411,
                    2.0036,
                    2.8286,
                    0
                  ],
                  "y": [
                    0.7145,
                    -0.7145,
                    0,
                    0,
                    0
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 162201905,
        "version": 1
      },
      "source": {
        "db": {
          "name": "1088",
          "source_id": {
            "str": "X5993"
          }
        }
      },
      "synonyms": [
        "Ammonium nitrate",
        "X5993"
      ],
      "comment": [
        "[6484-52-2]"
      ],
      "xref": [
        {
          "regid": "X5993"
        },
        {
          "dburl": "http://www.aksci.com"
        },
        {
          "sburl": "http://www.aksci.com/item_detail.php?cat=X5993"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              1,
              2
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    2.1,
                    0,
                    2.1,
                    1.4,
                    0.7
                  ],
                  "y": [
                    2.4249,
                    1.2124,
                    0,
                    1.2124,
                    0
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 162630135,
        "version": 1
      },
      "source": {
        "db": {
          "name": "1096",
          "source_id": {
            "str": "CTK2F2930"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium nitrate",
        "CTK2F2930"
      ],
      "xref": [
        {
          "regid": "CTK2F2930"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.chemtik.com/"
        },
        {
          "sburl": "http://www.chemtik.com/pro_result/252930/"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9
            ],
            "element": [
              8,
              8,
              8,
              7,
              7,
              1,
              1,
              1,
              1
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3,
              4,
              4,
              4,
              4
            ],
            "aid2": [
              5,
              5,
              5,
              6,
              7,
              8,
              9
            ],
            "order": [
              1,
              1,
              2,
              1,
              1,
              1,
              1
            ]
          },
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 163805952,
        "version": 1
      },
      "source": {
        "db": {
          "name": "1137",
          "source_id": {
            "str": "KSC352S3B"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium nitrate",
        "KSC352S3B"
      ],
      "xref": [
        {
          "regid": "KSC352S3B"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.kingscientific.com"
        },
        {
          "sburl": "http://www.kingscientific.com/pro_result/10054/"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9
            ],
            "element": [
              8,
              8,
              8,
              7,
              7,
              1,
              1,
              1,
              1
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3,
              4,
              4,
              4,
              4
            ],
            "aid2": [
              5,
              5,
              5,
              6,
              7,
              8,
              9
            ],
            "order": [
              1,
              1,
              2,
              1,
              1,
              1,
              1
            ]
          },
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 176257587,
        "version": 1
      },
      "source": {
        "db": {
          "name": "2331",
          "source_id": {
            "str": "143297"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium nitrate",
        "Nitric acid ammonium salt (1:1)"
      ],
      "comment": [
        "MolecularFormula:  H3N.HNO3",
        "MolecularWeight:  80.04",
        "FormerCASRegistryNumberList:",
        "893438-76-1",
        "95255-40-6",
        "IncorrectlyUsedCASRegistryNumberList:",
        "7783-20-2",
        "SubstanceCreateDate:  2006-10-13 14:30:12.0",
        "SubstanceLastUpdateDate:  2010-02-17 10:28:51.0"
      ],
      "xref": [
        {
          "regid": "143297"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://iaspub.epa.gov/sor_internet/registry/substreg/"
        },
        {
          "sburl": "http://iaspub.epa.gov/sor_internet/registry/substreg/searchandretrieve/advancedsearch/externalSearch.do?p_type=SRSITN&p_value=143297"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              1,
              2
            ]
          },
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 204380269,
        "version": 3
      },
      "source": {
        "db": {
          "name": "Tractus",
          "source_id": {
            "str": "RT-000207"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium nitrate",
        "RT-000207"
      ],
      "xref": [
        {
          "regid": "RT-000207"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.tractuschem.com/productshow/RT-000207.html"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              1,
              2
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    3.2411,
                    3.2411,
                    2.0036,
                    2.8286,
                    0
                  ],
                  "y": [
                    0.7145,
                    -0.7145,
                    0,
                    0,
                    0
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 223756827,
        "version": 2
      },
      "source": {
        "db": {
          "name": "10590",
          "source_id": {
            "str": "DVARTQFDIMZBAA-UHFFFAOYSA-O"
          }
        }
      },
      "synonyms": [
        "DVARTQFDIMZBAA-UHFFFAOYSA-O",
        "ammonium nitrate"
      ],
      "comment": [
        "SMILES: [N+](=O)([O-])[O-].[NH4+]",
        "InChI: InChI=1S/NO3.H3N/c2-1(3)4;/h;1H3/q-1;/p+1",
        "InChI Key: DVARTQFDIMZBAA-UHFFFAOYSA-O"
      ],
      "xref": [
        {
          "regid": "DVARTQFDIMZBAA-UHFFFAOYSA-O"
        },
        {
          "dburl": "http://nextmovesoftware.com/"
        },
        {
          "patent": "US03953192"
        },
        {
          "patent": "US03967948"
        },
        {
          "patent": "US03978092"
        },
        {
          "patent": "US04005208"
        },
        {
          "patent": "US04035468"
        },
        {
          "patent": "US04061583"
        },
        {
          "patent": "US04337208"
        },
        {
          "patent": "US04339607"
        },
        {
          "patent": "US04353758"
        },
        {
          "patent": "US04384120"
        },
        {
          "patent": "US04402918"
        },
        {
          "patent": "US04421578"
        },
        {
          "patent": "US04438038"
        },
        {
          "patent": "US04466805"
        },
        {
          "patent": "US04540690"
        },
        {
          "patent": "US04638078"
        },
        {
          "patent": "US04652559"
        },
        {
          "patent": "US04680391"
        },
        {
          "patent": "US04788280"
        },
        {
          "patent": "US04826997"
        },
        {
          "patent": "US04867914"
        },
        {
          "patent": "US04898455"
        },
        {
          "patent": "US04952231"
        },
        {
          "patent": "US04965329"
        },
        {
          "patent": "US05019362"
        },
        {
          "patent": "US05037990"
        },
        {
          "patent": "US05098461"
        },
        {
          "patent": "US05173500"
        },
        {
          "patent": "US05202356"
        },
        {
          "patent": "US05216148"
        },
        {
          "patent": "US05229381"
        },
        {
          "patent": "US05292387"
        },
        {
          "patent": "US05300511"
        },
        {
          "patent": "US05308372"
        },
        {
          "patent": "US05336784"
        },
        {
          "patent": "US05395945"
        },
        {
          "patent": "US05405926"
        },
        {
          "patent": "US05521184"
        },
        {
          "patent": "US05543520"
        },
        {
          "patent": "US05545272"
        },
        {
          "patent": "US05556981"
        },
        {
          "patent": "US05569768"
        },
        {
          "patent": "US05591849"
        },
        {
          "patent": "US05612340"
        },
        {
          "patent": "US05612360"
        },
        {
          "patent": "US05616586"
        },
        {
          "patent": "US05624650"
        },
        {
          "patent": "US05633248"
        },
        {
          "patent": "US05641938"
        },
        {
          "patent": "US05646140"
        },
        {
          "patent": "US05675119"
        },
        {
          "patent": "US05681858"
        },
        {
          "patent": "US05693633"
        },
        {
          "patent": "US05705502"
        },
        {
          "patent": "US05714714"
        },
        {
          "patent": "US05739129"
        },
        {
          "patent": "US05795983"
        },
        {
          "patent": "US05910495"
        },
        {
          "patent": "US05965679"
        },
        {
          "patent": "US05972136"
        },
        {
          "patent": "US06002008"
        },
        {
          "patent": "US06024855"
        },
        {
          "patent": "US06036933"
        },
        {
          "patent": "US06043254"
        },
        {
          "patent": "US06048864"
        },
        {
          "patent": "US06051712"
        },
        {
          "patent": "US06150526"
        },
        {
          "patent": "US06241281B1"
        },
        {
          "patent": "US06288082B1"
        },
        {
          "patent": "US06288188B1"
        },
        {
          "patent": "US06297258B1"
        },
        {
          "patent": "US06297265B2"
        },
        {
          "patent": "US06355799B1"
        },
        {
          "patent": "US06384051B1"
        },
        {
          "patent": "US06417194B1"
        },
        {
          "patent": "US06419887B1"
        },
        {
          "patent": "US06528653B2"
        },
        {
          "patent": "US06531502B1"
        },
        {
          "patent": "US06545161B2"
        },
        {
          "patent": "US06632952B1"
        },
        {
          "patent": "US06689181B2"
        },
        {
          "patent": "US06761866B1"
        },
        {
          "patent": "US06777437B2"
        },
        {
          "patent": "US06822100B2"
        },
        {
          "patent": "US06835367B2"
        },
        {
          "patent": "US06855710B2"
        },
        {
          "patent": "US06855730B2"
        },
        {
          "patent": "US06906063B2"
        },
        {
          "patent": "US06972286B2"
        },
        {
          "patent": "US07026085B2"
        },
        {
          "patent": "US07029504B2"
        },
        {
          "patent": "US07056926B2"
        },
        {
          "patent": "US07151109B2"
        },
        {
          "patent": "US07169791B2"
        },
        {
          "patent": "US07175684B1"
        },
        {
          "patent": "US07175871B2"
        },
        {
          "patent": "US07255842B1"
        },
        {
          "patent": "US07279467B2"
        },
        {
          "patent": "US07358257B2"
        },
        {
          "patent": "US07465808B2"
        },
        {
          "patent": "US07465815B2"
        },
        {
          "patent": "US07495021B2"
        },
        {
          "patent": "US07514468B2"
        },
        {
          "patent": "US07534788B2"
        },
        {
          "patent": "US07550481B2"
        },
        {
          "patent": "US07553863B2"
        },
        {
          "patent": "US07569566B2"
        },
        {
          "patent": "US07622474B2"
        },
        {
          "patent": "US07897607B2"
        },
        {
          "patent": "US07902203B2"
        },
        {
          "patent": "US07956053B2"
        },
        {
          "patent": "US07968571B2"
        },
        {
          "patent": "US08030499B2"
        },
        {
          "patent": "US08067428B2"
        },
        {
          "patent": "US08084649B2"
        },
        {
          "patent": "US08106064B2"
        },
        {
          "patent": "US08163899B2"
        },
        {
          "patent": "US08309714B2"
        },
        {
          "patent": "US08317952B2"
        },
        {
          "patent": "US08318746B2"
        },
        {
          "patent": "US08394837B2"
        },
        {
          "patent": "US08445510B2"
        },
        {
          "patent": "US08471014B2"
        },
        {
          "patent": "US08481551B2"
        },
        {
          "patent": "US08481552B2"
        },
        {
          "patent": "US08507489B2"
        },
        {
          "patent": "US08524721B2"
        },
        {
          "patent": "US08530388B2"
        },
        {
          "patent": "US08536351B2"
        },
        {
          "patent": "US08580762B2"
        },
        {
          "patent": "US08586766B2"
        },
        {
          "patent": "US08617327B1"
        },
        {
          "patent": "US08629157B2"
        },
        {
          "patent": "US08629277B2"
        },
        {
          "patent": "US08680012B2"
        },
        {
          "patent": "US08729274B2"
        },
        {
          "patent": "US08735322B2"
        },
        {
          "patent": "US08741806B2"
        },
        {
          "patent": "US08754220B2"
        },
        {
          "patent": "US08809538B2"
        },
        {
          "patent": "US08828908B2"
        },
        {
          "patent": "US08912326B2"
        },
        {
          "patent": "US08940913B2"
        },
        {
          "patent": "US08969359B2"
        },
        {
          "patent": "US09006429B2"
        },
        {
          "patent": "US09096634B2"
        },
        {
          "patent": "US09108977B2"
        },
        {
          "patent": "US09133158B2"
        },
        {
          "patent": "US09409916B2"
        },
        {
          "patent": "US20010018447A1"
        },
        {
          "patent": "US20020028841A1"
        },
        {
          "patent": "US20020077486A1"
        },
        {
          "patent": "US20020095966A1"
        },
        {
          "patent": "US20020110517A1"
        },
        {
          "patent": "US20020133007A1"
        },
        {
          "patent": "US20020133021A1"
        },
        {
          "patent": "US20030073849A1"
        },
        {
          "patent": "US20030236422A1"
        },
        {
          "patent": "US20040002511A1"
        },
        {
          "patent": "US20040013779A1"
        },
        {
          "patent": "US20040024010A1"
        },
        {
          "patent": "US20040058978A1"
        },
        {
          "patent": "US20040067531A1"
        },
        {
          "patent": "US20040067960A1"
        },
        {
          "patent": "US20040098840A1"
        },
        {
          "patent": "US20040143003A1"
        },
        {
          "patent": "US20040162285A1"
        },
        {
          "patent": "US20040167123A1"
        },
        {
          "patent": "US20040176609A1"
        },
        {
          "patent": "US20040185361A1"
        },
        {
          "patent": "US20040186293A1"
        },
        {
          "patent": "US20050054655A1"
        },
        {
          "patent": "US20050075331A1"
        },
        {
          "patent": "US20050107419A1"
        },
        {
          "patent": "US20050176775A1"
        },
        {
          "patent": "US20050228029A1"
        },
        {
          "patent": "US20060040996A1"
        },
        {
          "patent": "US20060074119A1"
        },
        {
          "patent": "US20060079533A1"
        },
        {
          "patent": "US20060167015A1"
        },
        {
          "patent": "US20060194795A1"
        },
        {
          "patent": "US20060194813A1"
        },
        {
          "patent": "US20060247233A1"
        },
        {
          "patent": "US20060281736A1"
        },
        {
          "patent": "US20070053821A1"
        },
        {
          "patent": "US20070072894A1"
        },
        {
          "patent": "US20070093506A1"
        },
        {
          "patent": "US20070096350A1"
        },
        {
          "patent": "US20070099990A1"
        },
        {
          "patent": "US20070135454A1"
        },
        {
          "patent": "US20070142634A1"
        },
        {
          "patent": "US20070179165A1"
        },
        {
          "patent": "US20070207929A1"
        },
        {
          "patent": "US20070244330A1"
        },
        {
          "patent": "US20070255063A1"
        },
        {
          "patent": "US20070293487A1"
        },
        {
          "patent": "US20070293497A1"
        },
        {
          "patent": "US20070299092A1"
        },
        {
          "patent": "US20080004273A1"
        },
        {
          "patent": "US20080015233A1"
        },
        {
          "patent": "US20080070920A1"
        },
        {
          "patent": "US20080188451A1"
        },
        {
          "patent": "US20080194597A1"
        },
        {
          "patent": "US20080269298A1"
        },
        {
          "patent": "US20080318923A1"
        },
        {
          "patent": "US20090023800A1"
        },
        {
          "patent": "US20090029976A1"
        },
        {
          "patent": "US20090082345A1"
        },
        {
          "patent": "US20090131428A1"
        },
        {
          "patent": "US20090137596A1"
        },
        {
          "patent": "US20090197926A1"
        },
        {
          "patent": "US20090253685A1"
        },
        {
          "patent": "US20090258855A1"
        },
        {
          "patent": "US20090286821A1"
        },
        {
          "patent": "US20100113270A1"
        },
        {
          "patent": "US20100130446A1"
        },
        {
          "patent": "US20100173774A1"
        },
        {
          "patent": "US20100210466A1"
        },
        {
          "patent": "US20100210680A1"
        },
        {
          "patent": "US20100216638A1"
        },
        {
          "patent": "US20100234350A1"
        },
        {
          "patent": "US20100240743A1"
        },
        {
          "patent": "US20100267944A1"
        },
        {
          "patent": "US20100324283A1"
        },
        {
          "patent": "US20110118236A1"
        },
        {
          "patent": "US20110218187A1"
        },
        {
          "patent": "US20110237659A1"
        },
        {
          "patent": "US20110269744A1"
        },
        {
          "patent": "US20110275515A1"
        },
        {
          "patent": "US20110275608A1"
        },
        {
          "patent": "US20110281888A1"
        },
        {
          "patent": "US20120035053A1"
        },
        {
          "patent": "US20120103479A1"
        },
        {
          "patent": "US20120131972A1"
        },
        {
          "patent": "US20120142529A1"
        },
        {
          "patent": "US20120142625A1"
        },
        {
          "patent": "US20120142677A1"
        },
        {
          "patent": "US20120149688A1"
        },
        {
          "patent": "US20120184512A1"
        },
        {
          "patent": "US20120184741A1"
        },
        {
          "patent": "US20120184742A1"
        },
        {
          "patent": "US20120190545A1"
        },
        {
          "patent": "US20120232076A1"
        },
        {
          "patent": "US20120232122A1"
        },
        {
          "patent": "US20120309987A1"
        },
        {
          "patent": "US20130005771A1"
        },
        {
          "patent": "US20130012496A1"
        },
        {
          "patent": "US20130059837A1"
        },
        {
          "patent": "US20130143863A1"
        },
        {
          "patent": "US20130192323A1"
        },
        {
          "patent": "US20130253197A1"
        },
        {
          "patent": "US20130261305A1"
        },
        {
          "patent": "US20130289002A1"
        },
        {
          "patent": "US20130317222A1"
        },
        {
          "patent": "US20130327455A1"
        },
        {
          "patent": "US20140005389A1"
        },
        {
          "patent": "US20140011827A1"
        },
        {
          "patent": "US20140045791A1"
        },
        {
          "patent": "US20140051654A1"
        },
        {
          "patent": "US20140088114A1"
        },
        {
          "patent": "US20140221405A1"
        },
        {
          "patent": "US20140371283A1"
        },
        {
          "patent": "US20150315208A1"
        },
        {
          "patent": "US20150366893A1"
        },
        {
          "patent": "US20160009658A1"
        },
        {
          "patent": "US20160159746A1"
        },
        {
          "patent": "USRE039590E1"
        },
        {
          "patent": "USRE042376E1"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9
            ],
            "element": [
              8,
              8,
              8,
              7,
              7,
              1,
              1,
              1,
              1
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3,
              4,
              4,
              4,
              4
            ],
            "aid2": [
              5,
              5,
              5,
              6,
              7,
              8,
              9
            ],
            "order": [
              1,
              1,
              2,
              1,
              1,
              1,
              1
            ]
          },
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 312598256,
        "version": 1
      },
      "source": {
        "db": {
          "name": "731",
          "source_id": {
            "str": "098901"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium Nitrate"
      ],
      "xref": [
        {
          "regid": "098901"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.oakwoodchemical.com"
        },
        {
          "sburl": "http://www.oakwoodchemical.com/ProductsList.aspx?CategoryID=-2&txtSearch=161772&ExtHyperLink=1"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              1,
              2
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    0.7005,
                    -0.7421,
                    -0.0208,
                    -0.0208,
                    1.4962
                  ],
                  "y": [
                    -0.4123,
                    -0.4123,
                    0.8371,
                    0.0042,
                    0.1826
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 315444026,
        "version": 1
      },
      "source": {
        "db": {
          "name": "12093",
          "source_id": {
            "str": "12165767"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium nitrate"
      ],
      "xref": [
        {
          "regid": "12165767"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.phionchemicals.com"
        },
        {
          "sburl": "http://phionchemicals.com/product-tag/6484-52-2"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9
            ],
            "element": [
              8,
              8,
              8,
              7,
              7,
              1,
              1,
              1,
              1
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3,
              4,
              4,
              4,
              4
            ],
            "aid2": [
              5,
              5,
              5,
              6,
              7,
              8,
              9
            ],
            "order": [
              1,
              1,
              2,
              1,
              1,
              1,
              1
            ]
          },
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 315676640,
        "version": 2
      },
      "source": {
        "db": {
          "name": "EPA DSSTox",
          "source_id": {
            "str": "DTXSID2029668"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium nitrate",
        "DTXSID2029668"
      ],
      "comment": [
        "QC-Level: DSSTox_Low"
      ],
      "xref": [
        {
          "dburl": "https://www.epa.gov/chemical-research/distributed-structure-searchable-toxicity-dsstox-database"
        },
        {
          "sburl": "https://comptox.epa.gov/dashboard/DTXSID2029668"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "regid": "DTXSID2029668"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              7,
              8,
              8,
              8,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": 1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": -1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              1,
              1
            ],
            "aid2": [
              2,
              3,
              4
            ],
            "order": [
              1,
              2,
              1
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    1.5395,
                    2.3038,
                    2.3364,
                    0,
                    5.4208
                  ],
                  "y": [
                    -1.3173,
                    -2.6725,
                    0,
                    -1.2793,
                    -1.3336
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 316963322,
        "version": 1
      },
      "source": {
        "db": {
          "name": "15224",
          "source_id": {
            "str": "17396"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium Nitrate"
      ],
      "xref": [
        {
          "regid": "17396"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.parchem.com"
        },
        {
          "sburl": "http://www.parchem.com/chemical-supplier-distributor/Ammonium-Nitrate-007396.aspx"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9
            ],
            "element": [
              8,
              8,
              8,
              7,
              7,
              1,
              1,
              1,
              1
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3,
              4,
              4,
              4,
              4
            ],
            "aid2": [
              5,
              5,
              5,
              6,
              7,
              8,
              9
            ],
            "order": [
              1,
              1,
              2,
              1,
              1,
              1,
              1
            ]
          },
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 319078427,
        "version": 1
      },
      "source": {
        "db": {
          "name": "15207",
          "source_id": {
            "str": "ToxPlanet-NjQ4NC01Mi0yMjI5ODU="
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "AMN (CHRIS Code)",
        "ANU (CHRIS Code)",
        "Ammonium nitrate",
        "Ammonium nitrate (solution)",
        "Ammonium nitrate, [with more than 0.2 percent combustible substances, including any organic substance calculated as carbon, to the exclusion of any other added substance]",
        "Ammonium nitrate, solid [nitrogen concentration of 23% nitrogen or greater]",
        "Ammonium nitricum",
        "Ammonium saltpeter",
        "Ammonium(I) nitrate (1:1)",
        "Caswell No. 045",
        "EC 229-347-8",
        "EINECS 229-347-8",
        "EPA Pesticide Chemical Code 076101",
        "German saltpeter",
        "H3-N.H-N-O3",
        "H3N.HNO3",
        "HSDB 475",
        "Herco prills",
        "Merco Prills",
        "NA0222",
        "NA0223",
        "NA0331",
        "NA1479",
        "NA1760",
        "NA1942",
        "NA2067",
        "NA2071",
        "NA2072",
        "NA2426",
        "NA3375",
        "Nitram",
        "Nitrate d'ammonium",
        "Nitrate d'ammonium [French]",
        "Nitrate of ammonia",
        "Nitrato amonico",
        "Nitrato amonico [Spanish]",
        "Nitric acid ammonium salt",
        "Nitric acid ammonium salt (1:1)",
        "Nitric acid amonium salt",
        "Nitric acid, ammonium salt",
        "Norway saltpeter",
        "UN0222",
        "UN0223",
        "UN0331",
        "UN1479",
        "UN1760",
        "UN1942",
        "UN2067",
        "UN2070",
        "UN2071",
        "UN2072",
        "UN2426",
        "UN3375",
        "UNII-T8YA51M7Y6",
        "Varioform I"
      ],
      "xref": [
        {
          "regid": "ToxPlanet-NjQ4NC01Mi0yMjI5ODU="
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "https:/www/toxplanet.com"
        },
        {
          "sburl": "https://search.toxplanet.com/CategorySearch.aspx?cas_no=6484-52-2"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9
            ],
            "element": [
              8,
              8,
              8,
              7,
              7,
              1,
              1,
              1,
              1
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3,
              4,
              4,
              4,
              4
            ],
            "aid2": [
              5,
              5,
              5,
              6,
              7,
              8,
              9
            ],
            "order": [
              1,
              1,
              2,
              1,
              1,
              1,
              1
            ]
          },
          "coords": [
            {
              "type": [
                1,
                5,
                255
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
              ],
              "conformers": [
                {
                  "x": [
                    1.732,
                    0,
                    0.866,
                    0.866,
                    0.866,
                    1.403,
                    0.3291,
                    0.556,
                    1.176
                  ],
                  "y": [
                    1.5,
                    1.5,
                    0,
                    4.0369,
                    1,
                    4.3469,
                    3.7269,
                    4.5739,
                    3.5
                  ]
                }
              ]
            }
          ],
          "charge": 0,
          "count": {
            "heavy_atom": 5,
            "atom_chiral": 0,
            "atom_chiral_def": 0,
            "atom_chiral_undef": 0,
            "bond_chiral": 0,
            "bond_chiral_def": 0,
            "bond_chiral_undef": 0,
            "isotope_atom": 0,
            "covalent_unit": 2,
            "tautomers": 1
          }
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 336352160,
        "version": 1
      },
      "source": {
        "db": {
          "name": "940",
          "source_id": {
            "str": "AGN-PC-0TE42P"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium nitrate"
      ],
      "xref": [
        {
          "regid": "AGN-PC-0TE42P"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.angenechemical.com"
        },
        {
          "sburl": "http://www.angenechemical.com/productshow/AGN-PC-0TE42P.html"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9
            ],
            "element": [
              8,
              8,
              8,
              7,
              7,
              1,
              1,
              1,
              1
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3,
              4,
              4,
              4,
              4
            ],
            "aid2": [
              5,
              5,
              5,
              6,
              7,
              8,
              9
            ],
            "order": [
              1,
              1,
              2,
              1,
              1,
              1,
              1
            ]
          },
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 341139253,
        "version": 1
      },
      "source": {
        "db": {
          "name": "15745",
          "source_id": {
            "str": "5039028-533425430"
          }
        }
      },
      "synonyms": [
        "ammonium nitrate"
      ],
      "comment": [
        "This substance has the INFOCHEM hashcode: 5039028-533425430"
      ],
      "xref": [
        {
          "regid": "5039028-533425430"
        },
        {
          "dburl": "https://link.springer.com"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              1,
              2
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    1.1828,
                    -0.0477,
                    -1.1828,
                    0,
                    0
                  ],
                  "y": [
                    -2,
                    -0.0349,
                    -2,
                    -1.3736,
                    2
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 342388582,
        "version": 1
      },
      "source": {
        "db": {
          "name": "15747",
          "source_id": {
            "str": "WB437068ST"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium nitrate"
      ],
      "xref": [
        {
          "regid": "WB437068ST"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.wubei-biochem.com/"
        },
        {
          "sburl": "http://wubei-biochem.com/product/506360"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9
            ],
            "element": [
              8,
              8,
              8,
              7,
              7,
              1,
              1,
              1,
              1
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3,
              4,
              4,
              4,
              4
            ],
            "aid2": [
              5,
              5,
              5,
              6,
              7,
              8,
              9
            ],
            "order": [
              1,
              1,
              2,
              1,
              1,
              1,
              1
            ]
          },
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 349997697,
        "version": 1
      },
      "source": {
        "db": {
          "name": "20885",
          "source_id": {
            "str": "A676212"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium Nitrate"
      ],
      "xref": [
        {
          "regid": "A676212"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "https://www.fishersci.com/us/en/brands/I8T3NQD9/fisher-chemical.html"
        },
        {
          "sburl": "https://www.fishersci.com/shop/products/ammonium-nitrate-granular-certified-acs-fisher-chemical-2/p-30976"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9
            ],
            "element": [
              8,
              8,
              8,
              7,
              7,
              1,
              1,
              1,
              1
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3,
              4,
              4,
              4,
              4
            ],
            "aid2": [
              5,
              5,
              5,
              6,
              7,
              8,
              9
            ],
            "order": [
              1,
              1,
              2,
              1,
              1,
              1,
              1
            ]
          },
          "coords": [
            {
              "type": [
                1,
                5,
                255
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
              ],
              "conformers": [
                {
                  "x": [
                    1.732,
                    0,
                    0.866,
                    0.866,
                    0.866,
                    1.403,
                    0.3291,
                    0.556,
                    1.176
                  ],
                  "y": [
                    1.5,
                    1.5,
                    0,
                    4.0369,
                    1,
                    4.3469,
                    3.7269,
                    4.5739,
                    3.5
                  ]
                }
              ]
            }
          ],
          "charge": 0,
          "count": {
            "heavy_atom": 5,
            "atom_chiral": 0,
            "atom_chiral_def": 0,
            "atom_chiral_undef": 0,
            "bond_chiral": 0,
            "bond_chiral_def": 0,
            "bond_chiral_undef": 0,
            "isotope_atom": 0,
            "covalent_unit": 2,
            "tautomers": 1
          }
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 349997698,
        "version": 1
      },
      "source": {
        "db": {
          "name": "20885",
          "source_id": {
            "str": "A676500"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium Nitrate"
      ],
      "xref": [
        {
          "regid": "A676500"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "https://www.fishersci.com/us/en/brands/I8T3NQD9/fisher-chemical.html"
        },
        {
          "sburl": "https://www.fishersci.com/shop/products/ammonium-nitrate-granular-certified-acs-fisher-chemical-2/p-30976"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9
            ],
            "element": [
              8,
              8,
              8,
              7,
              7,
              1,
              1,
              1,
              1
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3,
              4,
              4,
              4,
              4
            ],
            "aid2": [
              5,
              5,
              5,
              6,
              7,
              8,
              9
            ],
            "order": [
              1,
              1,
              2,
              1,
              1,
              1,
              1
            ]
          },
          "coords": [
            {
              "type": [
                1,
                5,
                255
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
              ],
              "conformers": [
                {
                  "x": [
                    1.732,
                    0,
                    0.866,
                    0.866,
                    0.866,
                    1.403,
                    0.3291,
                    0.556,
                    1.176
                  ],
                  "y": [
                    1.5,
                    1.5,
                    0,
                    4.0369,
                    1,
                    4.3469,
                    3.7269,
                    4.5739,
                    3.5
                  ]
                }
              ]
            }
          ],
          "charge": 0,
          "count": {
            "heavy_atom": 5,
            "atom_chiral": 0,
            "atom_chiral_def": 0,
            "atom_chiral_undef": 0,
            "bond_chiral": 0,
            "bond_chiral_def": 0,
            "bond_chiral_undef": 0,
            "isotope_atom": 0,
            "covalent_unit": 2,
            "tautomers": 1
          }
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 374190437,
        "version": 1
      },
      "source": {
        "db": {
          "name": "21014",
          "source_id": {
            "str": "AA006SFN"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium nitrate"
      ],
      "xref": [
        {
          "regid": "AA006SFN"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.aablocks.com"
        },
        {
          "sburl": "http://www.aablocks.com/goods/Goods/detail?id=AA006SFN"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9
            ],
            "element": [
              8,
              8,
              8,
              7,
              7,
              1,
              1,
              1,
              1
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3,
              4,
              4,
              4,
              4
            ],
            "aid2": [
              5,
              5,
              5,
              6,
              7,
              8,
              9
            ],
            "order": [
              1,
              1,
              2,
              1,
              1,
              1,
              1
            ]
          },
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 376073389,
        "version": 15
      },
      "source": {
        "db": {
          "name": "Comparative Toxicogenomics Database",
          "source_id": {
            "str": "C006568"
          }
        }
      },
      "synonyms": [
        "ammonium nitrate",
        "6484-52-2",
        "C006568"
      ],
      "comment": [
        "The Comparative Toxicogenomics Database (CTD) promotes understanding about the effects of environmental chemicals",
        "on human health by curating chemical-gene/protein interactions and chemical- and gene-disease relationships from",
        "the literature.  Click on these links to find specific, curated data for this chemical at CTD:",
        "Genes and Proteins http://ctdbase.org/detail.go?view=gene&type=chem&acc=C006568",
        "Chemical-Gene Interactions http://ctdbase.org/detail.go?view=ixn&type=chem&acc=C006568",
        "Pathways http://ctdbase.org/detail.go?view=pathway&type=chem&acc=C006568",
        "Depositor-supplied synonyms are taken from MeSH (Medical Subject Headings)."
      ],
      "xref": [
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://ctdbase.org/"
        },
        {
          "sburl": "http://ctdbase.org/detail.go?type=chem&acc=C006568"
        },
        {
          "gene": 3553
        },
        {
          "pmid": 29953848
        },
        {
          "taxonomy": 9606
        },
        {
          "regid": "C006568"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "props": [
            {
              "urn": {
                "label": "AutoGenerated",
                "name": "Structure",
                "datatype": 1,
                "version": "2.1",
                "software": "PubChem",
                "source": "ncbi.nlm.nih.gov",
                "release": "2019.06.18"
              },
              "value": {
                "sval": "Deposited Substance chemical structure was generated via Synonym(s) \"AMMONIUM NITRATE\" and MeSH to be CID 22985"
              }
            }
          ]
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 383235031,
        "version": 1
      },
      "source": {
        "db": {
          "name": "11777",
          "source_id": {
            "str": "NSTH-MA01109"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium nitrate"
      ],
      "xref": [
        {
          "regid": "NSTH-MA01109"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.norris-pharm.com/"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              1,
              2
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    3.2411,
                    3.2411,
                    2.0036,
                    2.8286,
                    0
                  ],
                  "y": [
                    0.7145,
                    -0.7145,
                    0,
                    0,
                    0
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 385643953,
        "version": 1
      },
      "source": {
        "db": {
          "name": "1139",
          "source_id": {
            "str": "Q182329"
          }
        }
      },
      "synonyms": [
        "ammonium nitrate",
        "Q182329"
      ],
      "xref": [
        {
          "dburl": "http://chem-bla-ics.blogspot.com/"
        },
        {
          "sburl": "https://tools.wmflabs.org/scholia/Q182329"
        },
        {
          "regid": "Q182329"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9
            ],
            "element": [
              7,
              1,
              1,
              1,
              1,
              7,
              8,
              8,
              8
            ],
            "charge": [
              {
                "aid": 1,
                "value": 1
              },
              {
                "aid": 6,
                "value": 1
              },
              {
                "aid": 8,
                "value": -1
              },
              {
                "aid": 9,
                "value": -1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              1,
              1,
              1,
              6,
              6,
              6
            ],
            "aid2": [
              2,
              3,
              4,
              5,
              7,
              8,
              9
            ],
            "order": [
              1,
              1,
              1,
              1,
              2,
              1,
              1
            ]
          },
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 386268853,
        "version": 1
      },
      "source": {
        "db": {
          "name": "23690",
          "source_id": {
            "str": "123681"
          }
        }
      },
      "synonyms": [
        "ammonium nitrate"
      ],
      "xref": [
        {
          "dburl": "https://onlinelibrary.wiley.com/"
        },
        {
          "regid": "123681"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              7,
              8,
              8,
              8,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": 1
              },
              {
                "aid": 3,
                "value": -1
              },
              {
                "aid": 4,
                "value": -1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              1,
              1
            ],
            "aid2": [
              2,
              3,
              4
            ],
            "order": [
              2,
              1,
              1
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    0,
                    1.1828,
                    -1.1828,
                    -0.0477,
                    0
                  ],
                  "y": [
                    -1.3736,
                    -2,
                    -2,
                    -0.035,
                    2
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 386480262,
        "version": 1
      },
      "source": {
        "db": {
          "name": "23756",
          "source_id": {
            "str": "Q182329"
          }
        }
      },
      "synonyms": [
        "ammonium nitrate"
      ],
      "xref": [
        {
          "dburl": "https://wikidata.org/"
        },
        {
          "sburl": "https://tools.wmflabs.org/scholia/Q182329"
        },
        {
          "regid": "Q182329"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9
            ],
            "element": [
              7,
              1,
              1,
              1,
              1,
              7,
              8,
              8,
              8
            ],
            "charge": [
              {
                "aid": 1,
                "value": 1
              },
              {
                "aid": 6,
                "value": 1
              },
              {
                "aid": 8,
                "value": -1
              },
              {
                "aid": 9,
                "value": -1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              1,
              1,
              1,
              6,
              6,
              6
            ],
            "aid2": [
              2,
              3,
              4,
              5,
              7,
              8,
              9
            ],
            "order": [
              1,
              1,
              1,
              1,
              2,
              1,
              1
            ]
          },
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 387086723,
        "version": 7
      },
      "source": {
        "db": {
          "name": "23819",
          "source_id": {
            "str": "DVARTQFDIMZBAA-UHFFFAOYSA-O"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium nitrate"
      ],
      "comment": [
        "DOI:10.5281/zenodo.3653160"
      ],
      "xref": [
        {
          "dburl": "https://www.norman-network.com/nds/SLE/"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "regid": "DVARTQFDIMZBAA-UHFFFAOYSA-O"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9
            ],
            "element": [
              8,
              8,
              8,
              7,
              7,
              1,
              1,
              1,
              1
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3,
              4,
              4,
              4,
              4
            ],
            "aid2": [
              5,
              5,
              5,
              6,
              7,
              8,
              9
            ],
            "order": [
              1,
              1,
              2,
              1,
              1,
              1,
              1
            ]
          },
          "coords": [
            {
              "type": [
                1,
                5,
                255
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
              ],
              "conformers": [
                {
                  "x": [
                    0,
                    0.866,
                    1.732,
                    0.866,
                    0.866,
                    1.403,
                    0.3291,
                    0.556,
                    1.176
                  ],
                  "y": [
                    1.5,
                    0,
                    1.5,
                    4.0369,
                    1,
                    4.3469,
                    3.7269,
                    4.5739,
                    3.5
                  ]
                }
              ]
            }
          ],
          "charge": 0,
          "count": {
            "heavy_atom": 5,
            "atom_chiral": 0,
            "atom_chiral_def": 0,
            "atom_chiral_undef": 0,
            "bond_chiral": 0,
            "bond_chiral_def": 0,
            "bond_chiral_undef": 0,
            "isotope_atom": 0,
            "covalent_unit": 2,
            "tautomers": -1
          }
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 402330504,
        "version": 1
      },
      "source": {
        "db": {
          "name": "23514",
          "source_id": {
            "str": "EM1.01187.5000"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "AMMONIUM NITRATE 6484-52-2 E-PURE 5 KG",
        "Ammonium nitrate"
      ],
      "xref": [
        {
          "dburl": "https://www.avantorinc.com/"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "sburl": "https://us.vwr.com/store/product/18724211/ammonium-nitrate"
        },
        {
          "regid": "EM1.01187.5000"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "props": [
            {
              "urn": {
                "label": "AutoGenerated",
                "name": "Structure",
                "datatype": 1,
                "version": "2.1",
                "software": "PubChem",
                "source": "ncbi.nlm.nih.gov",
                "release": "2019.06.18"
              },
              "value": {
                "sval": "Deposited Substance chemical structure was generated via Synonym(s) \"AMMONIUM NITRATE\" and MeSH to be CID 22985"
              }
            }
          ]
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 405236845,
        "version": 1
      },
      "source": {
        "db": {
          "name": "BioCyc",
          "source_id": {
            "str": "CPD-22959"
          }
        }
      },
      "synonyms": [
        "ammonium nitrate"
      ],
      "comment": [
        "TYPES: Inorganic-Salts"
      ],
      "xref": [
        {
          "dburl": "https://biocyc.org/"
        },
        {
          "sburl": "https://biocyc.org/compound?orgid=META&id=CPD-22959"
        },
        {
          "regid": "CPD-22959"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "props": [
            {
              "urn": {
                "label": "AutoGenerated",
                "name": "Structure",
                "datatype": 1,
                "version": "2.1",
                "software": "PubChem",
                "source": "ncbi.nlm.nih.gov",
                "release": "2019.06.18"
              },
              "value": {
                "sval": "Deposited Substance chemical structure was generated via Synonym(s) \"AMMONIUM NITRATE\" and MeSH to be CID 22985"
              }
            }
          ]
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 22985
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 85083774,
        "version": 1
      },
      "source": {
        "db": {
          "name": "MP Biomedicals",
          "source_id": {
            "str": "154776"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "AMMONIUM NITRATE"
      ],
      "xref": [
        {
          "regid": "154776"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.mpbio.com"
        },
        {
          "sburl": "http://www.mpbio.com/product_info.php?open=&cPath=&selecttab=&family_key=02154776"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              2,
              1
            ]
          },
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 13417569
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 310266792,
        "version": 2
      },
      "source": {
        "db": {
          "name": "11995",
          "source_id": {
            "str": "GK0937"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium nitrate",
        "MFCD00011425"
      ],
      "xref": [
        {
          "regid": "GK0937"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.glentham.com"
        },
        {
          "sburl": "http://www.glentham.com/products/product/GK0937/"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              2,
              1
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    -1.1596,
                    -1.1596,
                    0.0866,
                    -0.7475,
                    1.1596
                  ],
                  "y": [
                    -0.9207,
                    0.5066,
                    -0.212,
                    -0.206,
                    0.9207
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 13417569
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 349853420,
        "version": 1
      },
      "source": {
        "db": {
          "name": "15494",
          "source_id": {
            "str": "PBCM1371565"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium nitrate"
      ],
      "xref": [
        {
          "regid": "PBCM1371565"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.chemieliva.com"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              2,
              2,
              1
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    3.5,
                    2,
                    2,
                    2.5,
                    0
                  ],
                  "y": [
                    -0,
                    -0.866,
                    0.866,
                    -0,
                    0
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 13417569
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 375088355,
        "version": 1
      },
      "source": {
        "db": {
          "name": "20980",
          "source_id": {
            "str": "3B4-2045"
          }
        }
      },
      "synonyms": [
        "6484-52-2",
        "Ammonium nitrate",
        "nitric acid, ammonia salt"
      ],
      "xref": [
        {
          "regid": "3B4-2045"
        },
        {
          "rn": "6484-52-2"
        },
        {
          "dburl": "http://www.3bsc.com"
        },
        {
          "sburl": "http://www.3bsc.com/index/pro_info.php?id=66125"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "charge": [
              {
                "aid": 1,
                "value": -1
              },
              {
                "aid": 4,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              1,
              2,
              1
            ]
          },
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 13417569
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 944
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 10531706,
        "version": 1
      },
      "source": {
        "db": {
          "name": "NIST Chemistry WebBook",
          "source_id": {
            "str": "2138210556"
          }
        }
      },
      "synonyms": [
        "Ammonium nitrate"
      ],
      "xref": [
        {
          "regid": "2138210556"
        },
        {
          "dburl": "http://webbook.nist.gov/chemistry/"
        },
        {
          "sburl": "http://webbook.nist.gov/cgi/cbook.cgi?InChI=InChI%3D1/H4N2O3/c1-5-2%283%294/h1H4%0A"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9
            ],
            "element": [
              8,
              8,
              8,
              7,
              7,
              1,
              1,
              1,
              1
            ],
            "charge": [
              {
                "aid": 2,
                "value": -1
              },
              {
                "aid": 5,
                "value": 1
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              1,
              2,
              3,
              4,
              4,
              4,
              4
            ],
            "aid2": [
              4,
              5,
              5,
              5,
              6,
              7,
              8,
              9
            ],
            "order": [
              1,
              1,
              1,
              2,
              1,
              1,
              1,
              1
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
              ],
              "conformers": [
                {
                  "x": [
                    1.4766,
                    0.7144,
                    0,
                    2.1312,
                    0.7144,
                    2.8934,
                    2.0235,
                    2.4469,
                    2.8436
                  ],
                  "y": [
                    0.5093,
                    0,
                    1.2375,
                    1.0115,
                    0.825,
                    0.6958,
                    1.8295,
                    0.2493,
                    1.4292
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 6327609
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 6327610
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 50810448,
        "version": 2
      },
      "source": {
        "db": {
          "name": "NextBio",
          "source_id": {
            "str": "6327609"
          }
        }
      },
      "synonyms": [
        "Ammonium Nitrate",
        "CID6327609"
      ],
      "xref": [
        {
          "regid": "6327609"
        },
        {
          "dburl": "http://www.nextbio.com/"
        },
        {
          "sburl": "http://www.nextbio.com/b/search/ov/Ammonium+Nitrate?id=7982745&type=compound&synonym=Ammonium+Nitrate"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "props": [
            {
              "urn": {
                "label": "AutoGenerated",
                "name": "Structure",
                "datatype": 1,
                "version": "2.1",
                "software": "PubChem",
                "source": "ncbi.nlm.nih.gov",
                "release": "2011.04.04"
              },
              "value": {
                "sval": "Deposited Substance chemical structure was generated via Synonym \"CID6327609\" to be CID 6327609"
              }
            }
          ]
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 6327609
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 6327610
            }
          }
        }
      ]
    },
    {
      "sid": {
        "id": 348968041,
        "version": 1
      },
      "source": {
        "db": {
          "name": "15494",
          "source_id": {
            "str": "PBCM0486192"
          }
        }
      },
      "synonyms": [
        "31432-46-9",
        "Ammonium nitrate"
      ],
      "xref": [
        {
          "regid": "PBCM0486192"
        },
        {
          "rn": "31432-46-9"
        },
        {
          "dburl": "http://www.chemieliva.com"
        }
      ],
      "compound": [
        {
          "id": {
            "type": 0
          },
          "atoms": {
            "aid": [
              1,
              2,
              3,
              4,
              5
            ],
            "element": [
              8,
              8,
              8,
              7,
              7
            ],
            "isotope": [
              {
                "aid": 4,
                "value": 15
              }
            ]
          },
          "bonds": {
            "aid1": [
              1,
              2,
              3
            ],
            "aid2": [
              4,
              4,
              4
            ],
            "order": [
              2,
              2,
              1
            ]
          },
          "coords": [
            {
              "type": [
                1,
                3
              ],
              "aid": [
                1,
                2,
                3,
                4,
                5
              ],
              "conformers": [
                {
                  "x": [
                    3.5,
                    2,
                    2,
                    2.5,
                    0
                  ],
                  "y": [
                    -0,
                    -0.866,
                    0.866,
                    -0,
                    0
                  ]
                }
              ]
            }
          ],
          "charge": 0
        },
        {
          "id": {
            "type": 1,
            "id": {
              "cid": 53393587
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 222
            }
          }
        },
        {
          "id": {
            "type": 2,
            "id": {
              "cid": 10313048
            }
          }
        }
      ]
    }
  ]
}

cidstring = stringsearch(json.dumps(newvar), "cid")
print(cidstring)