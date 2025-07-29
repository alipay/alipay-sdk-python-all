#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApartmentContactInfo(object):

    def __init__(self):
        self._contact_alipay_account = None
        self._contact_name = None
        self._contact_profile_pic = None
        self._enabled_lead_channels = None
        self._im_url = None
        self._mobile = None

    @property
    def contact_alipay_account(self):
        return self._contact_alipay_account

    @contact_alipay_account.setter
    def contact_alipay_account(self, value):
        self._contact_alipay_account = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def contact_profile_pic(self):
        return self._contact_profile_pic

    @contact_profile_pic.setter
    def contact_profile_pic(self, value):
        self._contact_profile_pic = value
    @property
    def enabled_lead_channels(self):
        return self._enabled_lead_channels

    @enabled_lead_channels.setter
    def enabled_lead_channels(self, value):
        if isinstance(value, list):
            self._enabled_lead_channels = list()
            for i in value:
                self._enabled_lead_channels.append(i)
    @property
    def im_url(self):
        return self._im_url

    @im_url.setter
    def im_url(self, value):
        self._im_url = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_alipay_account:
            if hasattr(self.contact_alipay_account, 'to_alipay_dict'):
                params['contact_alipay_account'] = self.contact_alipay_account.to_alipay_dict()
            else:
                params['contact_alipay_account'] = self.contact_alipay_account
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.contact_profile_pic:
            if hasattr(self.contact_profile_pic, 'to_alipay_dict'):
                params['contact_profile_pic'] = self.contact_profile_pic.to_alipay_dict()
            else:
                params['contact_profile_pic'] = self.contact_profile_pic
        if self.enabled_lead_channels:
            if isinstance(self.enabled_lead_channels, list):
                for i in range(0, len(self.enabled_lead_channels)):
                    element = self.enabled_lead_channels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.enabled_lead_channels[i] = element.to_alipay_dict()
            if hasattr(self.enabled_lead_channels, 'to_alipay_dict'):
                params['enabled_lead_channels'] = self.enabled_lead_channels.to_alipay_dict()
            else:
                params['enabled_lead_channels'] = self.enabled_lead_channels
        if self.im_url:
            if hasattr(self.im_url, 'to_alipay_dict'):
                params['im_url'] = self.im_url.to_alipay_dict()
            else:
                params['im_url'] = self.im_url
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApartmentContactInfo()
        if 'contact_alipay_account' in d:
            o.contact_alipay_account = d['contact_alipay_account']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'contact_profile_pic' in d:
            o.contact_profile_pic = d['contact_profile_pic']
        if 'enabled_lead_channels' in d:
            o.enabled_lead_channels = d['enabled_lead_channels']
        if 'im_url' in d:
            o.im_url = d['im_url']
        if 'mobile' in d:
            o.mobile = d['mobile']
        return o


