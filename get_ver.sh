#!/bin/sh

echo -n '<div style="border: 1px dashed #cccccc; background-color : #f5f5f5; padding: 10px;">'
python -V
pip list |grep ango
echo '</div>'
