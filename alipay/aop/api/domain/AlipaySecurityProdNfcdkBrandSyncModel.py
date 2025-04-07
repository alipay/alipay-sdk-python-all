#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdNfcdkBrandSyncModel(object):

    def __init__(self):
        self._account_name = None
        self._action = None
        self._ble_name = None
        self._channel = None
        self._dk_info = None
        self._dk_max_count = None
        self._end_time = None
        self._key_id = None
        self._key_type = None
        self._mac = None
        self._master_account_no = None
        self._master_key_id = None
        self._mobile_no = None
        self._nfc_info = None
        self._protocol_type = None
        self._start_time = None
        self._status = None
        self._time = None
        self._tuid = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def ble_name(self):
        return self._ble_name

    @ble_name.setter
    def ble_name(self, value):
        self._ble_name = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def dk_info(self):
        return self._dk_info

    @dk_info.setter
    def dk_info(self, value):
        self._dk_info = value
    @property
    def dk_max_count(self):
        return self._dk_max_count

    @dk_max_count.setter
    def dk_max_count(self, value):
        self._dk_max_count = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def key_id(self):
        return self._key_id

    @key_id.setter
    def key_id(self, value):
        self._key_id = value
    @property
    def key_type(self):
        return self._key_type

    @key_type.setter
    def key_type(self, value):
        self._key_type = value
    @property
    def mac(self):
        return self._mac

    @mac.setter
    def mac(self, value):
        self._mac = value
    @property
    def master_account_no(self):
        return self._master_account_no

    @master_account_no.setter
    def master_account_no(self, value):
        self._master_account_no = value
    @property
    def master_key_id(self):
        return self._master_key_id

    @master_key_id.setter
    def master_key_id(self, value):
        self._master_key_id = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def nfc_info(self):
        return self._nfc_info

    @nfc_info.setter
    def nfc_info(self, value):
        self._nfc_info = value
    @property
    def protocol_type(self):
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, value):
        self._protocol_type = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
    @property
    def tuid(self):
        return self._tuid

    @tuid.setter
    def tuid(self, value):
        self._tuid = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.ble_name:
            if hasattr(self.ble_name, 'to_alipay_dict'):
                params['ble_name'] = self.ble_name.to_alipay_dict()
            else:
                params['ble_name'] = self.ble_name
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.dk_info:
            if hasattr(self.dk_info, 'to_alipay_dict'):
                params['dk_info'] = self.dk_info.to_alipay_dict()
            else:
                params['dk_info'] = self.dk_info
        if self.dk_max_count:
            if hasattr(self.dk_max_count, 'to_alipay_dict'):
                params['dk_max_count'] = self.dk_max_count.to_alipay_dict()
            else:
                params['dk_max_count'] = self.dk_max_count
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.key_id:
            if hasattr(self.key_id, 'to_alipay_dict'):
                params['key_id'] = self.key_id.to_alipay_dict()
            else:
                params['key_id'] = self.key_id
        if self.key_type:
            if hasattr(self.key_type, 'to_alipay_dict'):
                params['key_type'] = self.key_type.to_alipay_dict()
            else:
                params['key_type'] = self.key_type
        if self.mac:
            if hasattr(self.mac, 'to_alipay_dict'):
                params['mac'] = self.mac.to_alipay_dict()
            else:
                params['mac'] = self.mac
        if self.master_account_no:
            if hasattr(self.master_account_no, 'to_alipay_dict'):
                params['master_account_no'] = self.master_account_no.to_alipay_dict()
            else:
                params['master_account_no'] = self.master_account_no
        if self.master_key_id:
            if hasattr(self.master_key_id, 'to_alipay_dict'):
                params['master_key_id'] = self.master_key_id.to_alipay_dict()
            else:
                params['master_key_id'] = self.master_key_id
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.nfc_info:
            if hasattr(self.nfc_info, 'to_alipay_dict'):
                params['nfc_info'] = self.nfc_info.to_alipay_dict()
            else:
                params['nfc_info'] = self.nfc_info
        if self.protocol_type:
            if hasattr(self.protocol_type, 'to_alipay_dict'):
                params['protocol_type'] = self.protocol_type.to_alipay_dict()
            else:
                params['protocol_type'] = self.protocol_type
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        if self.tuid:
            if hasattr(self.tuid, 'to_alipay_dict'):
                params['tuid'] = self.tuid.to_alipay_dict()
            else:
                params['tuid'] = self.tuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdNfcdkBrandSyncModel()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'action' in d:
            o.action = d['action']
        if 'ble_name' in d:
            o.ble_name = d['ble_name']
        if 'channel' in d:
            o.channel = d['channel']
        if 'dk_info' in d:
            o.dk_info = d['dk_info']
        if 'dk_max_count' in d:
            o.dk_max_count = d['dk_max_count']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'key_id' in d:
            o.key_id = d['key_id']
        if 'key_type' in d:
            o.key_type = d['key_type']
        if 'mac' in d:
            o.mac = d['mac']
        if 'master_account_no' in d:
            o.master_account_no = d['master_account_no']
        if 'master_key_id' in d:
            o.master_key_id = d['master_key_id']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'nfc_info' in d:
            o.nfc_info = d['nfc_info']
        if 'protocol_type' in d:
            o.protocol_type = d['protocol_type']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'time' in d:
            o.time = d['time']
        if 'tuid' in d:
            o.tuid = d['tuid']
        return o


