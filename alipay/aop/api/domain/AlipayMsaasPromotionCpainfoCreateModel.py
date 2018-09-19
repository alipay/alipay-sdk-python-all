#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasPromotionCpainfoCreateModel(object):

    def __init__(self):
        self._app_id = None
        self._app_version = None
        self._bundle_id = None
        self._channel_id = None
        self._debug = None
        self._extend = None
        self._idfa = None
        self._ios_version = None
        self._mac = None

    @property
    def app_id(self):
        return self._app_id

    @app_id.setter
    def app_id(self, value):
        self._app_id = value
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, value):
        self._debug = value
    @property
    def extend(self):
        return self._extend

    @extend.setter
    def extend(self, value):
        self._extend = value
    @property
    def idfa(self):
        return self._idfa

    @idfa.setter
    def idfa(self, value):
        self._idfa = value
    @property
    def ios_version(self):
        return self._ios_version

    @ios_version.setter
    def ios_version(self, value):
        self._ios_version = value
    @property
    def mac(self):
        return self._mac

    @mac.setter
    def mac(self, value):
        self._mac = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_id:
            if hasattr(self.app_id, 'to_alipay_dict'):
                params['app_id'] = self.app_id.to_alipay_dict()
            else:
                params['app_id'] = self.app_id
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.debug:
            if hasattr(self.debug, 'to_alipay_dict'):
                params['debug'] = self.debug.to_alipay_dict()
            else:
                params['debug'] = self.debug
        if self.extend:
            if hasattr(self.extend, 'to_alipay_dict'):
                params['extend'] = self.extend.to_alipay_dict()
            else:
                params['extend'] = self.extend
        if self.idfa:
            if hasattr(self.idfa, 'to_alipay_dict'):
                params['idfa'] = self.idfa.to_alipay_dict()
            else:
                params['idfa'] = self.idfa
        if self.ios_version:
            if hasattr(self.ios_version, 'to_alipay_dict'):
                params['ios_version'] = self.ios_version.to_alipay_dict()
            else:
                params['ios_version'] = self.ios_version
        if self.mac:
            if hasattr(self.mac, 'to_alipay_dict'):
                params['mac'] = self.mac.to_alipay_dict()
            else:
                params['mac'] = self.mac
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasPromotionCpainfoCreateModel()
        if 'app_id' in d:
            o.app_id = d['app_id']
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'debug' in d:
            o.debug = d['debug']
        if 'extend' in d:
            o.extend = d['extend']
        if 'idfa' in d:
            o.idfa = d['idfa']
        if 'ios_version' in d:
            o.ios_version = d['ios_version']
        if 'mac' in d:
            o.mac = d['mac']
        return o


