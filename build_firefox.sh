mkdir tmp_dist
rm -fr build dist
python setup_firefox.py bdist_wheel --plat-name manylinux_2_34_x86_64
mv dist/*.whl tmp_dist/
#
rm -fr build dist
python setup_firefox.py bdist_wheel --plat-name win_amd64
mv dist/*.whl tmp_dist/
#
rm -fr build dist
python setup_firefox.py bdist_wheel --plat-name macosx_10_9_x86_64
mv dist/*.whl tmp_dist/
#
rm -fr build dist
python setup_firefox.py bdist_wheel --plat-name macosx_11_0_arm64
mv dist/*.whl tmp_dist/
#
rm -fr build dist
python setup_firefox.py bdist_wheel --plat-name manylinux_2_34_aarch64
mv tmp_dist/* dist/
#
rmdir tmp_dist
