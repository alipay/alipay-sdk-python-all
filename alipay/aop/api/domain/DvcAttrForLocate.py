#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DvcAttrForLocate(object):

    def __init__(self):
        self._bluetooth_mac = None
        self._mall_group_cid = None
        self._mall_group_name = None
        self._poi_address = None
        self._poi_city_name = None
        self._poi_district_name = None
        self._poi_id = None
        self._poi_latitude = None
        self._poi_longitude = None
        self._poi_name = None
        self._poi_province_name = None
        self._scanned_ble_info = None
        self._scanned_cdma_info = None
        self._scanned_gsm_info = None
        self._scanned_lte_info = None
        self._scanned_wcdma_info = None
        self._scanned_wifi_info = None

    @property
    def bluetooth_mac(self):
        return self._bluetooth_mac

    @bluetooth_mac.setter
    def bluetooth_mac(self, value):
        self._bluetooth_mac = value
    @property
    def mall_group_cid(self):
        return self._mall_group_cid

    @mall_group_cid.setter
    def mall_group_cid(self, value):
        self._mall_group_cid = value
    @property
    def mall_group_name(self):
        return self._mall_group_name

    @mall_group_name.setter
    def mall_group_name(self, value):
        self._mall_group_name = value
    @property
    def poi_address(self):
        return self._poi_address

    @poi_address.setter
    def poi_address(self, value):
        self._poi_address = value
    @property
    def poi_city_name(self):
        return self._poi_city_name

    @poi_city_name.setter
    def poi_city_name(self, value):
        self._poi_city_name = value
    @property
    def poi_district_name(self):
        return self._poi_district_name

    @poi_district_name.setter
    def poi_district_name(self, value):
        self._poi_district_name = value
    @property
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value
    @property
    def poi_latitude(self):
        return self._poi_latitude

    @poi_latitude.setter
    def poi_latitude(self, value):
        self._poi_latitude = value
    @property
    def poi_longitude(self):
        return self._poi_longitude

    @poi_longitude.setter
    def poi_longitude(self, value):
        self._poi_longitude = value
    @property
    def poi_name(self):
        return self._poi_name

    @poi_name.setter
    def poi_name(self, value):
        self._poi_name = value
    @property
    def poi_province_name(self):
        return self._poi_province_name

    @poi_province_name.setter
    def poi_province_name(self, value):
        self._poi_province_name = value
    @property
    def scanned_ble_info(self):
        return self._scanned_ble_info

    @scanned_ble_info.setter
    def scanned_ble_info(self, value):
        self._scanned_ble_info = value
    @property
    def scanned_cdma_info(self):
        return self._scanned_cdma_info

    @scanned_cdma_info.setter
    def scanned_cdma_info(self, value):
        self._scanned_cdma_info = value
    @property
    def scanned_gsm_info(self):
        return self._scanned_gsm_info

    @scanned_gsm_info.setter
    def scanned_gsm_info(self, value):
        self._scanned_gsm_info = value
    @property
    def scanned_lte_info(self):
        return self._scanned_lte_info

    @scanned_lte_info.setter
    def scanned_lte_info(self, value):
        self._scanned_lte_info = value
    @property
    def scanned_wcdma_info(self):
        return self._scanned_wcdma_info

    @scanned_wcdma_info.setter
    def scanned_wcdma_info(self, value):
        self._scanned_wcdma_info = value
    @property
    def scanned_wifi_info(self):
        return self._scanned_wifi_info

    @scanned_wifi_info.setter
    def scanned_wifi_info(self, value):
        self._scanned_wifi_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.bluetooth_mac:
            if hasattr(self.bluetooth_mac, 'to_alipay_dict'):
                params['bluetooth_mac'] = self.bluetooth_mac.to_alipay_dict()
            else:
                params['bluetooth_mac'] = self.bluetooth_mac
        if self.mall_group_cid:
            if hasattr(self.mall_group_cid, 'to_alipay_dict'):
                params['mall_group_cid'] = self.mall_group_cid.to_alipay_dict()
            else:
                params['mall_group_cid'] = self.mall_group_cid
        if self.mall_group_name:
            if hasattr(self.mall_group_name, 'to_alipay_dict'):
                params['mall_group_name'] = self.mall_group_name.to_alipay_dict()
            else:
                params['mall_group_name'] = self.mall_group_name
        if self.poi_address:
            if hasattr(self.poi_address, 'to_alipay_dict'):
                params['poi_address'] = self.poi_address.to_alipay_dict()
            else:
                params['poi_address'] = self.poi_address
        if self.poi_city_name:
            if hasattr(self.poi_city_name, 'to_alipay_dict'):
                params['poi_city_name'] = self.poi_city_name.to_alipay_dict()
            else:
                params['poi_city_name'] = self.poi_city_name
        if self.poi_district_name:
            if hasattr(self.poi_district_name, 'to_alipay_dict'):
                params['poi_district_name'] = self.poi_district_name.to_alipay_dict()
            else:
                params['poi_district_name'] = self.poi_district_name
        if self.poi_id:
            if hasattr(self.poi_id, 'to_alipay_dict'):
                params['poi_id'] = self.poi_id.to_alipay_dict()
            else:
                params['poi_id'] = self.poi_id
        if self.poi_latitude:
            if hasattr(self.poi_latitude, 'to_alipay_dict'):
                params['poi_latitude'] = self.poi_latitude.to_alipay_dict()
            else:
                params['poi_latitude'] = self.poi_latitude
        if self.poi_longitude:
            if hasattr(self.poi_longitude, 'to_alipay_dict'):
                params['poi_longitude'] = self.poi_longitude.to_alipay_dict()
            else:
                params['poi_longitude'] = self.poi_longitude
        if self.poi_name:
            if hasattr(self.poi_name, 'to_alipay_dict'):
                params['poi_name'] = self.poi_name.to_alipay_dict()
            else:
                params['poi_name'] = self.poi_name
        if self.poi_province_name:
            if hasattr(self.poi_province_name, 'to_alipay_dict'):
                params['poi_province_name'] = self.poi_province_name.to_alipay_dict()
            else:
                params['poi_province_name'] = self.poi_province_name
        if self.scanned_ble_info:
            if hasattr(self.scanned_ble_info, 'to_alipay_dict'):
                params['scanned_ble_info'] = self.scanned_ble_info.to_alipay_dict()
            else:
                params['scanned_ble_info'] = self.scanned_ble_info
        if self.scanned_cdma_info:
            if hasattr(self.scanned_cdma_info, 'to_alipay_dict'):
                params['scanned_cdma_info'] = self.scanned_cdma_info.to_alipay_dict()
            else:
                params['scanned_cdma_info'] = self.scanned_cdma_info
        if self.scanned_gsm_info:
            if hasattr(self.scanned_gsm_info, 'to_alipay_dict'):
                params['scanned_gsm_info'] = self.scanned_gsm_info.to_alipay_dict()
            else:
                params['scanned_gsm_info'] = self.scanned_gsm_info
        if self.scanned_lte_info:
            if hasattr(self.scanned_lte_info, 'to_alipay_dict'):
                params['scanned_lte_info'] = self.scanned_lte_info.to_alipay_dict()
            else:
                params['scanned_lte_info'] = self.scanned_lte_info
        if self.scanned_wcdma_info:
            if hasattr(self.scanned_wcdma_info, 'to_alipay_dict'):
                params['scanned_wcdma_info'] = self.scanned_wcdma_info.to_alipay_dict()
            else:
                params['scanned_wcdma_info'] = self.scanned_wcdma_info
        if self.scanned_wifi_info:
            if hasattr(self.scanned_wifi_info, 'to_alipay_dict'):
                params['scanned_wifi_info'] = self.scanned_wifi_info.to_alipay_dict()
            else:
                params['scanned_wifi_info'] = self.scanned_wifi_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DvcAttrForLocate()
        if 'bluetooth_mac' in d:
            o.bluetooth_mac = d['bluetooth_mac']
        if 'mall_group_cid' in d:
            o.mall_group_cid = d['mall_group_cid']
        if 'mall_group_name' in d:
            o.mall_group_name = d['mall_group_name']
        if 'poi_address' in d:
            o.poi_address = d['poi_address']
        if 'poi_city_name' in d:
            o.poi_city_name = d['poi_city_name']
        if 'poi_district_name' in d:
            o.poi_district_name = d['poi_district_name']
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        if 'poi_latitude' in d:
            o.poi_latitude = d['poi_latitude']
        if 'poi_longitude' in d:
            o.poi_longitude = d['poi_longitude']
        if 'poi_name' in d:
            o.poi_name = d['poi_name']
        if 'poi_province_name' in d:
            o.poi_province_name = d['poi_province_name']
        if 'scanned_ble_info' in d:
            o.scanned_ble_info = d['scanned_ble_info']
        if 'scanned_cdma_info' in d:
            o.scanned_cdma_info = d['scanned_cdma_info']
        if 'scanned_gsm_info' in d:
            o.scanned_gsm_info = d['scanned_gsm_info']
        if 'scanned_lte_info' in d:
            o.scanned_lte_info = d['scanned_lte_info']
        if 'scanned_wcdma_info' in d:
            o.scanned_wcdma_info = d['scanned_wcdma_info']
        if 'scanned_wifi_info' in d:
            o.scanned_wifi_info = d['scanned_wifi_info']
        return o


