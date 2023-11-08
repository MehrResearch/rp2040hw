#    Copyright 2023 Hessam Mehr

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from uctypes import BF_POS, BF_LEN, BFUINT32, ARRAY, UINT32, struct

SYSINFO_BASE = const(0x40000000)

CHIP_ID_FIELDS = {
    'REVISION': 28 << BF_POS | 4 << BF_LEN | UINT32,
    'PART': 12 << BF_POS | 16 << BF_LEN | UINT32,
    'MANUFACTURER': 0 << BF_POS | 12 << BF_LEN | UINT32,
}

PLATFORM_FIELDS = {
    'ASIC': 1 << BF_POS | 1 << BF_LEN | UINT32,
    'FPGA': 0 << BF_POS | 1 << BF_LEN | UINT32,
}

SYSINFO_FIELDS = {
    'CHIP_ID': (0x00, CHIP_ID_FIELDS),
    'PLATFORM': (0x04, PLATFORM_FIELDS),
    'GITREF_RP2040': (0x40, UINT32),
}

sysinfo = struct(SYSINFO_BASE, SYSINFO_FIELDS)