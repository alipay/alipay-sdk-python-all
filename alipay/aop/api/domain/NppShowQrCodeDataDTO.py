#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NppQrCodeDTO import NppQrCodeDTO


class NppShowQrCodeDataDTO(object):

    def __init__(self):
        self._address_des = None
        self._goods_des = None
        self._placard_url = None
        self._qr_code_list = None
        self._time_des = None

    @property
    def address_des(self):
        return self._address_des

    @address_des.setter
    def address_des(self, value):
        self._address_des = value
    @property
    def goods_des(self):
        return self._goods_des

    @goods_des.setter
    def goods_des(self, value):
        self._goods_des = value
    @property
    def placard_url(self):
        return self._placard_url

    @placard_url.setter
    def placard_url(self, value):
        self._placard_url = value
    @property
    def qr_code_list(self):
        return self._qr_code_list

    @qr_code_list.setter
    def qr_code_list(self, value):
        if isinstance(value, list):
            self._qr_code_list = list()
            for i in value:
                if isinstance(i, NppQrCodeDTO):
                    self._qr_code_list.append(i)
                else:
                    self._qr_code_list.append(NppQrCodeDTO.from_alipay_dict(i))
    @property
    def time_des(self):
        return self._time_des

    @time_des.setter
    def time_des(self, value):
        self._time_des = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_des:
            if hasattr(self.address_des, 'to_alipay_dict'):
                params['address_des'] = self.address_des.to_alipay_dict()
            else:
                params['address_des'] = self.address_des
        if self.goods_des:
            if hasattr(self.goods_des, 'to_alipay_dict'):
                params['goods_des'] = self.goods_des.to_alipay_dict()
            else:
                params['goods_des'] = self.goods_des
        if self.placard_url:
            if hasattr(self.placard_url, 'to_alipay_dict'):
                params['placard_url'] = self.placard_url.to_alipay_dict()
            else:
                params['placard_url'] = self.placard_url
        if self.qr_code_list:
            if isinstance(self.qr_code_list, list):
                for i in range(0, len(self.qr_code_list)):
                    element = self.qr_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.qr_code_list[i] = element.to_alipay_dict()
            if hasattr(self.qr_code_list, 'to_alipay_dict'):
                params['qr_code_list'] = self.qr_code_list.to_alipay_dict()
            else:
                params['qr_code_list'] = self.qr_code_list
        if self.time_des:
            if hasattr(self.time_des, 'to_alipay_dict'):
                params['time_des'] = self.time_des.to_alipay_dict()
            else:
                params['time_des'] = self.time_des
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NppShowQrCodeDataDTO()
        if 'address_des' in d:
            o.address_des = d['address_des']
        if 'goods_des' in d:
            o.goods_des = d['goods_des']
        if 'placard_url' in d:
            o.placard_url = d['placard_url']
        if 'qr_code_list' in d:
            o.qr_code_list = d['qr_code_list']
        if 'time_des' in d:
            o.time_des = d['time_des']
        return o


