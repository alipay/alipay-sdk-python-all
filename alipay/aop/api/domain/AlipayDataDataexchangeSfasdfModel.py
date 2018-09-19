#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipayItemVoucherTemplete import AlipayItemVoucherTemplete


class AlipayDataDataexchangeSfasdfModel(object):

    def __init__(self):
        self._adsfghjf = None
        self._easadasfd = None
        self._gdfsa = None
        self._hjgdfs = None
        self._sdfgsdfg = None
        self._wehtegf = None

    @property
    def adsfghjf(self):
        return self._adsfghjf

    @adsfghjf.setter
    def adsfghjf(self, value):
        if isinstance(value, AlipayItemVoucherTemplete):
            self._adsfghjf = value
        else:
            self._adsfghjf = AlipayItemVoucherTemplete.from_alipay_dict(value)
    @property
    def easadasfd(self):
        return self._easadasfd

    @easadasfd.setter
    def easadasfd(self, value):
        if isinstance(value, list):
            self._easadasfd = list()
            for i in value:
                self._easadasfd.append(i)
    @property
    def gdfsa(self):
        return self._gdfsa

    @gdfsa.setter
    def gdfsa(self, value):
        if isinstance(value, list):
            self._gdfsa = list()
            for i in value:
                self._gdfsa.append(i)
    @property
    def hjgdfs(self):
        return self._hjgdfs

    @hjgdfs.setter
    def hjgdfs(self, value):
        self._hjgdfs = value
    @property
    def sdfgsdfg(self):
        return self._sdfgsdfg

    @sdfgsdfg.setter
    def sdfgsdfg(self, value):
        if isinstance(value, list):
            self._sdfgsdfg = list()
            for i in value:
                self._sdfgsdfg.append(i)
    @property
    def wehtegf(self):
        return self._wehtegf

    @wehtegf.setter
    def wehtegf(self, value):
        if isinstance(value, list):
            self._wehtegf = list()
            for i in value:
                self._wehtegf.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.adsfghjf:
            if hasattr(self.adsfghjf, 'to_alipay_dict'):
                params['adsfghjf'] = self.adsfghjf.to_alipay_dict()
            else:
                params['adsfghjf'] = self.adsfghjf
        if self.easadasfd:
            if isinstance(self.easadasfd, list):
                for i in range(0, len(self.easadasfd)):
                    element = self.easadasfd[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.easadasfd[i] = element.to_alipay_dict()
            if hasattr(self.easadasfd, 'to_alipay_dict'):
                params['easadasfd'] = self.easadasfd.to_alipay_dict()
            else:
                params['easadasfd'] = self.easadasfd
        if self.gdfsa:
            if isinstance(self.gdfsa, list):
                for i in range(0, len(self.gdfsa)):
                    element = self.gdfsa[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.gdfsa[i] = element.to_alipay_dict()
            if hasattr(self.gdfsa, 'to_alipay_dict'):
                params['gdfsa'] = self.gdfsa.to_alipay_dict()
            else:
                params['gdfsa'] = self.gdfsa
        if self.hjgdfs:
            if hasattr(self.hjgdfs, 'to_alipay_dict'):
                params['hjgdfs'] = self.hjgdfs.to_alipay_dict()
            else:
                params['hjgdfs'] = self.hjgdfs
        if self.sdfgsdfg:
            if isinstance(self.sdfgsdfg, list):
                for i in range(0, len(self.sdfgsdfg)):
                    element = self.sdfgsdfg[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sdfgsdfg[i] = element.to_alipay_dict()
            if hasattr(self.sdfgsdfg, 'to_alipay_dict'):
                params['sdfgsdfg'] = self.sdfgsdfg.to_alipay_dict()
            else:
                params['sdfgsdfg'] = self.sdfgsdfg
        if self.wehtegf:
            if isinstance(self.wehtegf, list):
                for i in range(0, len(self.wehtegf)):
                    element = self.wehtegf[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.wehtegf[i] = element.to_alipay_dict()
            if hasattr(self.wehtegf, 'to_alipay_dict'):
                params['wehtegf'] = self.wehtegf.to_alipay_dict()
            else:
                params['wehtegf'] = self.wehtegf
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataexchangeSfasdfModel()
        if 'adsfghjf' in d:
            o.adsfghjf = d['adsfghjf']
        if 'easadasfd' in d:
            o.easadasfd = d['easadasfd']
        if 'gdfsa' in d:
            o.gdfsa = d['gdfsa']
        if 'hjgdfs' in d:
            o.hjgdfs = d['hjgdfs']
        if 'sdfgsdfg' in d:
            o.sdfgsdfg = d['sdfgsdfg']
        if 'wehtegf' in d:
            o.wehtegf = d['wehtegf']
        return o


