#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TourOrderSyncResponse(object):

    def __init__(self):
        self._open_id = None
        self._out_biz_no = None
        self._out_voucher_id = None
        self._user_id = None
        self._vid = None
        self._voucher_user_ids = None
        self._vourcher_user_ids = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_voucher_id(self):
        return self._out_voucher_id

    @out_voucher_id.setter
    def out_voucher_id(self, value):
        self._out_voucher_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def vid(self):
        return self._vid

    @vid.setter
    def vid(self, value):
        self._vid = value
    @property
    def voucher_user_ids(self):
        return self._voucher_user_ids

    @voucher_user_ids.setter
    def voucher_user_ids(self, value):
        if isinstance(value, list):
            self._voucher_user_ids = list()
            for i in value:
                self._voucher_user_ids.append(i)
    @property
    def vourcher_user_ids(self):
        return self._vourcher_user_ids

    @vourcher_user_ids.setter
    def vourcher_user_ids(self, value):
        if isinstance(value, list):
            self._vourcher_user_ids = list()
            for i in value:
                self._vourcher_user_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_voucher_id:
            if hasattr(self.out_voucher_id, 'to_alipay_dict'):
                params['out_voucher_id'] = self.out_voucher_id.to_alipay_dict()
            else:
                params['out_voucher_id'] = self.out_voucher_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.vid:
            if hasattr(self.vid, 'to_alipay_dict'):
                params['vid'] = self.vid.to_alipay_dict()
            else:
                params['vid'] = self.vid
        if self.voucher_user_ids:
            if isinstance(self.voucher_user_ids, list):
                for i in range(0, len(self.voucher_user_ids)):
                    element = self.voucher_user_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_user_ids[i] = element.to_alipay_dict()
            if hasattr(self.voucher_user_ids, 'to_alipay_dict'):
                params['voucher_user_ids'] = self.voucher_user_ids.to_alipay_dict()
            else:
                params['voucher_user_ids'] = self.voucher_user_ids
        if self.vourcher_user_ids:
            if isinstance(self.vourcher_user_ids, list):
                for i in range(0, len(self.vourcher_user_ids)):
                    element = self.vourcher_user_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.vourcher_user_ids[i] = element.to_alipay_dict()
            if hasattr(self.vourcher_user_ids, 'to_alipay_dict'):
                params['vourcher_user_ids'] = self.vourcher_user_ids.to_alipay_dict()
            else:
                params['vourcher_user_ids'] = self.vourcher_user_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TourOrderSyncResponse()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_voucher_id' in d:
            o.out_voucher_id = d['out_voucher_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'vid' in d:
            o.vid = d['vid']
        if 'voucher_user_ids' in d:
            o.voucher_user_ids = d['voucher_user_ids']
        if 'vourcher_user_ids' in d:
            o.vourcher_user_ids = d['vourcher_user_ids']
        return o


