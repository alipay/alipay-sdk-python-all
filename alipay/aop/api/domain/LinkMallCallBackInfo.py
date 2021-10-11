#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LinkMallCallBackInfo(object):

    def __init__(self):
        self._action = None
        self._bizid = None
        self._extinfo = None
        self._lmuserid = None
        self._promotionid = None
        self._promotioninstanceid = None
        self._taobaoid = None
        self._time_stamp = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def bizid(self):
        return self._bizid

    @bizid.setter
    def bizid(self, value):
        self._bizid = value
    @property
    def extinfo(self):
        return self._extinfo

    @extinfo.setter
    def extinfo(self, value):
        self._extinfo = value
    @property
    def lmuserid(self):
        return self._lmuserid

    @lmuserid.setter
    def lmuserid(self, value):
        self._lmuserid = value
    @property
    def promotionid(self):
        return self._promotionid

    @promotionid.setter
    def promotionid(self, value):
        self._promotionid = value
    @property
    def promotioninstanceid(self):
        return self._promotioninstanceid

    @promotioninstanceid.setter
    def promotioninstanceid(self, value):
        self._promotioninstanceid = value
    @property
    def taobaoid(self):
        return self._taobaoid

    @taobaoid.setter
    def taobaoid(self, value):
        self._taobaoid = value
    @property
    def time_stamp(self):
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, value):
        self._time_stamp = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.bizid:
            if hasattr(self.bizid, 'to_alipay_dict'):
                params['bizid'] = self.bizid.to_alipay_dict()
            else:
                params['bizid'] = self.bizid
        if self.extinfo:
            if hasattr(self.extinfo, 'to_alipay_dict'):
                params['extinfo'] = self.extinfo.to_alipay_dict()
            else:
                params['extinfo'] = self.extinfo
        if self.lmuserid:
            if hasattr(self.lmuserid, 'to_alipay_dict'):
                params['lmuserid'] = self.lmuserid.to_alipay_dict()
            else:
                params['lmuserid'] = self.lmuserid
        if self.promotionid:
            if hasattr(self.promotionid, 'to_alipay_dict'):
                params['promotionid'] = self.promotionid.to_alipay_dict()
            else:
                params['promotionid'] = self.promotionid
        if self.promotioninstanceid:
            if hasattr(self.promotioninstanceid, 'to_alipay_dict'):
                params['promotioninstanceid'] = self.promotioninstanceid.to_alipay_dict()
            else:
                params['promotioninstanceid'] = self.promotioninstanceid
        if self.taobaoid:
            if hasattr(self.taobaoid, 'to_alipay_dict'):
                params['taobaoid'] = self.taobaoid.to_alipay_dict()
            else:
                params['taobaoid'] = self.taobaoid
        if self.time_stamp:
            if hasattr(self.time_stamp, 'to_alipay_dict'):
                params['time_stamp'] = self.time_stamp.to_alipay_dict()
            else:
                params['time_stamp'] = self.time_stamp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LinkMallCallBackInfo()
        if 'action' in d:
            o.action = d['action']
        if 'bizid' in d:
            o.bizid = d['bizid']
        if 'extinfo' in d:
            o.extinfo = d['extinfo']
        if 'lmuserid' in d:
            o.lmuserid = d['lmuserid']
        if 'promotionid' in d:
            o.promotionid = d['promotionid']
        if 'promotioninstanceid' in d:
            o.promotioninstanceid = d['promotioninstanceid']
        if 'taobaoid' in d:
            o.taobaoid = d['taobaoid']
        if 'time_stamp' in d:
            o.time_stamp = d['time_stamp']
        return o


