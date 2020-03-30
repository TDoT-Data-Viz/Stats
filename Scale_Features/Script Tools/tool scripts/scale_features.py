import numpy as np



table = arcpy.GetParameterAsText(0)
infield = arcpy.GetParameterAsText(1)
min = arcpy.GetParameterAsText(2)
max = arcpy.GetParameterAsText(3)
outfield = arcpy.GetParameterAsText(4)

arcpy.AddField_management(table, outfield, "DOUBLE")
#arcpy.management.SelectLayerByAttribute(table, "NEW_SELECTION", "{} IS NOT NULL".format(infield), None)
arcpy.MakeTableView_management(table, "table_view", "{} IS NOT NULL".format(infield))
ta = arcpy.da.TableToNumPyArray("table_view", [infield])
arr = ta[infield]

min = float(min)
max = float(max)
rescaled = np.interp(arr, (arr.min(), arr.max()), (min, max))
i = 0
with arcpy.da.UpdateCursor("table_view", [outfield]) as cur:
    for row in cur:
        row[0] = rescaled[i]
        i += 1
        cur.updateRow(row)
del cur
