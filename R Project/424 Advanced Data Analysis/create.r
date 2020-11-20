heart_disease$Area_Rucc = ifelse(heart_disease$area__rucc == "Metro - Counties in metro areas of 1 million population or more","A1",
                            ifelse(heart_disease$area__rucc == "Metro - Counties in metro areas of 250,000 to 1 million population","A2",
                                   ifelse(heart_disease$area__rucc == "Metro - Counties in metro areas of fewer than 250,000 population","A3",
                                          ifelse(heart_disease$area__rucc == "Nonmetro - Urban population of 20,000 or more, adjacent to a metro area","C1",
                                                 ifelse(heart_disease$area__rucc == "Nonmetro - Urban population of 2,500 to 19,999, adjacent to a metro area","C2",
                                                        ifelse(heart_disease$area__rucc == "Nonmetro - Completely rural or less than 2,500 urban population, adjacent to a metro area","B1",
                                                               ifelse(heart_disease$area__rucc == "Nonmetro - Completely rural or less than 2,500 urban population, not adjacent to a metro area","B2",
                                                                      ifelse(heart_disease$area__rucc == "Nonmetro - Urban population of 20,000 or more, not adjacent to a metro area","D1","D2"))))))))

heart_disease$Area_Urban_Influence = ifelse(heart_disease$area__urban_influence == "Noncore adjacent to a small metro with town of at least 2,500 residents","N1",
                                 ifelse(heart_disease$area__urban_influence == "Noncore adjacent to a small metro and does not contain a town of at least 2,500 residents","N2",
                                        ifelse(heart_disease$area__urban_influence == "Noncore adjacent to micro area and contains a town of 2,500-19,999 residents","N3",
                                               ifelse(heart_disease$area__urban_influence == "Noncore adjacent to micro area and does not contain a town of at least 2,500 residents","N4",
                                                      ifelse(heart_disease$area__urban_influence == "Noncore not adjacent to a metro/micro area and contains a town of 2,500  or more residents","N5",
                                                             ifelse(heart_disease$area__urban_influence == "Noncore not adjacent to a metro/micro area and does not contain a town of at least","N6",
                                                                    ifelse(heart_disease$area__urban_influence == "Noncore adjacent to a large metro area","N7",
                                                                           ifelse(heart_disease$area__urban_influence == "Large-in a metro area with at least 1 million residents or more","M1",
                                                                                  ifelse(heart_disease$area__urban_influence == "Small-in a metro area with fewer than 1 million residents","M2",
                                                                                         ifelse(heart_disease$area__urban_influence == "Micropolitan adjacent to a large metro area","M3",
                                                                                                ifelse(heart_disease$area__urban_influence == "Micropolitan adjacent to a small metro area","M4","M5")))))))))))

heart_disease$Econ_Economic_typology = ifelse(heart_disease$econ__economic_typology == "Farm-dependent","Farm",
                                 ifelse(heart_disease$econ__economic_typology == "Federal/State government-dependent","Fed",
                                        ifelse(heart_disease$econ__economic_typology == "Manufacturing-dependent","Manu",
                                               ifelse(heart_disease$econ__economic_typology == "Mining-dependent","Mining",
                                                      ifelse(heart_disease$econ__economic_typology == "Nonspecialized","Nonsp","Recr")))))
heart_disease = heart_disease[,-c(2,3,4)]
heart_disease$Area_Rucc = as.factor(heart_disease$Area_Rucc)
heart_disease$Area_Urban_Influence = as.factor(heart_disease$Area_Urban_Influence)                                                           
heart_disease$Econ_Economic_typology = as.factor(heart_disease$Econ_Economic_typology)
