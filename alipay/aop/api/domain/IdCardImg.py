#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IdCardImg(object):

    def __init__(self):
        self._cardtype = None
        self._imgurls = None
        self._imgurltype = None

    @property
    def cardtype(self):
        return self._cardtype

    @cardtype.setter
    def cardtype(self, value):
        self._cardtype = value
    @property
    def imgurls(self):
        return self._imgurls

    @imgurls.setter
    def imgurls(self, value):
        self._imgurls = value
    @property
    def imgurltype(self):
        return self._imgurltype

    @imgurltype.setter
    def imgurltype(self, value):
        self._imgurltype = value


    def to_alipay_dict(self):
        params = dict()
        if self.cardtype:
            if hasattr(self.cardtype, 'to_alipay_dict'):
                params['cardtype'] = self.cardtype.to_alipay_dict()
            else:
                params['cardtype'] = self.cardtype
        if self.imgurls:
            if hasattr(self.imgurls, 'to_alipay_dict'):
                params['imgurls'] = self.imgurls.to_alipay_dict()
            else:
                params['imgurls'] = self.imgurls
        if self.imgurltype:
            if hasattr(self.imgurltype, 'to_alipay_dict'):
                params['imgurltype'] = self.imgurltype.to_alipay_dict()
            else:
                params['imgurltype'] = self.imgurltype
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IdCardImg()
        if 'cardtype' in d:
            o.cardtype = d['cardtype']
        if 'imgurls' in d:
            o.imgurls = d['imgurls']
        if 'imgurltype' in d:
            o.imgurltype = d['imgurltype']
        return o


