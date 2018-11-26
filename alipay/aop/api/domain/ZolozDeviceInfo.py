#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZolozDeviceInfo(object):

    def __init__(self):
        self._apdid = None
        self._app_name = None
        self._app_version = None
        self._cid = None
        self._h = None
        self._imei = None
        self._imsi = None
        self._ip = None
        self._lac = None
        self._latitude = None
        self._longitude = None
        self._mac = None
        self._mcc = None
        self._mnc = None
        self._model = None
        self._os = None
        self._px = None
        self._qemu = None
        self._release = None
        self._ret_code = None
        self._root = None
        self._rssi = None
        self._sdk_name = None
        self._sdk_version = None
        self._sn = None
        self._ssid = None
        self._success = None
        self._tid = None
        self._umid = None
        self._utdid = None
        self._w = None
        self._wireless_mac = None

    @property
    def apdid(self):
        return self._apdid

    @apdid.setter
    def apdid(self, value):
        self._apdid = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        self._cid = value
    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, value):
        self._h = value
    @property
    def imei(self):
        return self._imei

    @imei.setter
    def imei(self, value):
        self._imei = value
    @property
    def imsi(self):
        return self._imsi

    @imsi.setter
    def imsi(self, value):
        self._imsi = value
    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value
    @property
    def lac(self):
        return self._lac

    @lac.setter
    def lac(self, value):
        self._lac = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def mac(self):
        return self._mac

    @mac.setter
    def mac(self, value):
        self._mac = value
    @property
    def mcc(self):
        return self._mcc

    @mcc.setter
    def mcc(self, value):
        self._mcc = value
    @property
    def mnc(self):
        return self._mnc

    @mnc.setter
    def mnc(self, value):
        self._mnc = value
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value
    @property
    def os(self):
        return self._os

    @os.setter
    def os(self, value):
        self._os = value
    @property
    def px(self):
        return self._px

    @px.setter
    def px(self, value):
        self._px = value
    @property
    def qemu(self):
        return self._qemu

    @qemu.setter
    def qemu(self, value):
        self._qemu = value
    @property
    def release(self):
        return self._release

    @release.setter
    def release(self, value):
        self._release = value
    @property
    def ret_code(self):
        return self._ret_code

    @ret_code.setter
    def ret_code(self, value):
        self._ret_code = value
    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value
    @property
    def rssi(self):
        return self._rssi

    @rssi.setter
    def rssi(self, value):
        self._rssi = value
    @property
    def sdk_name(self):
        return self._sdk_name

    @sdk_name.setter
    def sdk_name(self, value):
        self._sdk_name = value
    @property
    def sdk_version(self):
        return self._sdk_version

    @sdk_version.setter
    def sdk_version(self, value):
        self._sdk_version = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def ssid(self):
        return self._ssid

    @ssid.setter
    def ssid(self, value):
        self._ssid = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def tid(self):
        return self._tid

    @tid.setter
    def tid(self, value):
        self._tid = value
    @property
    def umid(self):
        return self._umid

    @umid.setter
    def umid(self, value):
        self._umid = value
    @property
    def utdid(self):
        return self._utdid

    @utdid.setter
    def utdid(self, value):
        self._utdid = value
    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, value):
        self._w = value
    @property
    def wireless_mac(self):
        return self._wireless_mac

    @wireless_mac.setter
    def wireless_mac(self, value):
        self._wireless_mac = value


    def to_alipay_dict(self):
        params = dict()
        if self.apdid:
            if hasattr(self.apdid, 'to_alipay_dict'):
                params['apdid'] = self.apdid.to_alipay_dict()
            else:
                params['apdid'] = self.apdid
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.cid:
            if hasattr(self.cid, 'to_alipay_dict'):
                params['cid'] = self.cid.to_alipay_dict()
            else:
                params['cid'] = self.cid
        if self.h:
            if hasattr(self.h, 'to_alipay_dict'):
                params['h'] = self.h.to_alipay_dict()
            else:
                params['h'] = self.h
        if self.imei:
            if hasattr(self.imei, 'to_alipay_dict'):
                params['imei'] = self.imei.to_alipay_dict()
            else:
                params['imei'] = self.imei
        if self.imsi:
            if hasattr(self.imsi, 'to_alipay_dict'):
                params['imsi'] = self.imsi.to_alipay_dict()
            else:
                params['imsi'] = self.imsi
        if self.ip:
            if hasattr(self.ip, 'to_alipay_dict'):
                params['ip'] = self.ip.to_alipay_dict()
            else:
                params['ip'] = self.ip
        if self.lac:
            if hasattr(self.lac, 'to_alipay_dict'):
                params['lac'] = self.lac.to_alipay_dict()
            else:
                params['lac'] = self.lac
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.mac:
            if hasattr(self.mac, 'to_alipay_dict'):
                params['mac'] = self.mac.to_alipay_dict()
            else:
                params['mac'] = self.mac
        if self.mcc:
            if hasattr(self.mcc, 'to_alipay_dict'):
                params['mcc'] = self.mcc.to_alipay_dict()
            else:
                params['mcc'] = self.mcc
        if self.mnc:
            if hasattr(self.mnc, 'to_alipay_dict'):
                params['mnc'] = self.mnc.to_alipay_dict()
            else:
                params['mnc'] = self.mnc
        if self.model:
            if hasattr(self.model, 'to_alipay_dict'):
                params['model'] = self.model.to_alipay_dict()
            else:
                params['model'] = self.model
        if self.os:
            if hasattr(self.os, 'to_alipay_dict'):
                params['os'] = self.os.to_alipay_dict()
            else:
                params['os'] = self.os
        if self.px:
            if hasattr(self.px, 'to_alipay_dict'):
                params['px'] = self.px.to_alipay_dict()
            else:
                params['px'] = self.px
        if self.qemu:
            if hasattr(self.qemu, 'to_alipay_dict'):
                params['qemu'] = self.qemu.to_alipay_dict()
            else:
                params['qemu'] = self.qemu
        if self.release:
            if hasattr(self.release, 'to_alipay_dict'):
                params['release'] = self.release.to_alipay_dict()
            else:
                params['release'] = self.release
        if self.ret_code:
            if hasattr(self.ret_code, 'to_alipay_dict'):
                params['ret_code'] = self.ret_code.to_alipay_dict()
            else:
                params['ret_code'] = self.ret_code
        if self.root:
            if hasattr(self.root, 'to_alipay_dict'):
                params['root'] = self.root.to_alipay_dict()
            else:
                params['root'] = self.root
        if self.rssi:
            if hasattr(self.rssi, 'to_alipay_dict'):
                params['rssi'] = self.rssi.to_alipay_dict()
            else:
                params['rssi'] = self.rssi
        if self.sdk_name:
            if hasattr(self.sdk_name, 'to_alipay_dict'):
                params['sdk_name'] = self.sdk_name.to_alipay_dict()
            else:
                params['sdk_name'] = self.sdk_name
        if self.sdk_version:
            if hasattr(self.sdk_version, 'to_alipay_dict'):
                params['sdk_version'] = self.sdk_version.to_alipay_dict()
            else:
                params['sdk_version'] = self.sdk_version
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.ssid:
            if hasattr(self.ssid, 'to_alipay_dict'):
                params['ssid'] = self.ssid.to_alipay_dict()
            else:
                params['ssid'] = self.ssid
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        if self.tid:
            if hasattr(self.tid, 'to_alipay_dict'):
                params['tid'] = self.tid.to_alipay_dict()
            else:
                params['tid'] = self.tid
        if self.umid:
            if hasattr(self.umid, 'to_alipay_dict'):
                params['umid'] = self.umid.to_alipay_dict()
            else:
                params['umid'] = self.umid
        if self.utdid:
            if hasattr(self.utdid, 'to_alipay_dict'):
                params['utdid'] = self.utdid.to_alipay_dict()
            else:
                params['utdid'] = self.utdid
        if self.w:
            if hasattr(self.w, 'to_alipay_dict'):
                params['w'] = self.w.to_alipay_dict()
            else:
                params['w'] = self.w
        if self.wireless_mac:
            if hasattr(self.wireless_mac, 'to_alipay_dict'):
                params['wireless_mac'] = self.wireless_mac.to_alipay_dict()
            else:
                params['wireless_mac'] = self.wireless_mac
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozDeviceInfo()
        if 'apdid' in d:
            o.apdid = d['apdid']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'cid' in d:
            o.cid = d['cid']
        if 'h' in d:
            o.h = d['h']
        if 'imei' in d:
            o.imei = d['imei']
        if 'imsi' in d:
            o.imsi = d['imsi']
        if 'ip' in d:
            o.ip = d['ip']
        if 'lac' in d:
            o.lac = d['lac']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'mac' in d:
            o.mac = d['mac']
        if 'mcc' in d:
            o.mcc = d['mcc']
        if 'mnc' in d:
            o.mnc = d['mnc']
        if 'model' in d:
            o.model = d['model']
        if 'os' in d:
            o.os = d['os']
        if 'px' in d:
            o.px = d['px']
        if 'qemu' in d:
            o.qemu = d['qemu']
        if 'release' in d:
            o.release = d['release']
        if 'ret_code' in d:
            o.ret_code = d['ret_code']
        if 'root' in d:
            o.root = d['root']
        if 'rssi' in d:
            o.rssi = d['rssi']
        if 'sdk_name' in d:
            o.sdk_name = d['sdk_name']
        if 'sdk_version' in d:
            o.sdk_version = d['sdk_version']
        if 'sn' in d:
            o.sn = d['sn']
        if 'ssid' in d:
            o.ssid = d['ssid']
        if 'success' in d:
            o.success = d['success']
        if 'tid' in d:
            o.tid = d['tid']
        if 'umid' in d:
            o.umid = d['umid']
        if 'utdid' in d:
            o.utdid = d['utdid']
        if 'w' in d:
            o.w = d['w']
        if 'wireless_mac' in d:
            o.wireless_mac = d['wireless_mac']
        return o


