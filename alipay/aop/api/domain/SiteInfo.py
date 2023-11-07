#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SiteInfo(object):

    def __init__(self):
        self._account = None
        self._auth_letter_image = None
        self._download = None
        self._icp_no = None
        self._icp_org_name = None
        self._icp_service_name = None
        self._market = None
        self._password = None
        self._remark = None
        self._remark_image = None
        self._screenshot_image = None
        self._site_domain = None
        self._site_name = None
        self._site_type = None
        self._site_url = None
        self._status = None
        self._tiny_app_id = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def auth_letter_image(self):
        return self._auth_letter_image

    @auth_letter_image.setter
    def auth_letter_image(self, value):
        self._auth_letter_image = value
    @property
    def download(self):
        return self._download

    @download.setter
    def download(self, value):
        self._download = value
    @property
    def icp_no(self):
        return self._icp_no

    @icp_no.setter
    def icp_no(self, value):
        self._icp_no = value
    @property
    def icp_org_name(self):
        return self._icp_org_name

    @icp_org_name.setter
    def icp_org_name(self, value):
        self._icp_org_name = value
    @property
    def icp_service_name(self):
        return self._icp_service_name

    @icp_service_name.setter
    def icp_service_name(self, value):
        self._icp_service_name = value
    @property
    def market(self):
        return self._market

    @market.setter
    def market(self, value):
        self._market = value
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def remark_image(self):
        return self._remark_image

    @remark_image.setter
    def remark_image(self, value):
        self._remark_image = value
    @property
    def screenshot_image(self):
        return self._screenshot_image

    @screenshot_image.setter
    def screenshot_image(self, value):
        self._screenshot_image = value
    @property
    def site_domain(self):
        return self._site_domain

    @site_domain.setter
    def site_domain(self, value):
        self._site_domain = value
    @property
    def site_name(self):
        return self._site_name

    @site_name.setter
    def site_name(self, value):
        self._site_name = value
    @property
    def site_type(self):
        return self._site_type

    @site_type.setter
    def site_type(self, value):
        self._site_type = value
    @property
    def site_url(self):
        return self._site_url

    @site_url.setter
    def site_url(self, value):
        self._site_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tiny_app_id(self):
        return self._tiny_app_id

    @tiny_app_id.setter
    def tiny_app_id(self, value):
        self._tiny_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.auth_letter_image:
            if hasattr(self.auth_letter_image, 'to_alipay_dict'):
                params['auth_letter_image'] = self.auth_letter_image.to_alipay_dict()
            else:
                params['auth_letter_image'] = self.auth_letter_image
        if self.download:
            if hasattr(self.download, 'to_alipay_dict'):
                params['download'] = self.download.to_alipay_dict()
            else:
                params['download'] = self.download
        if self.icp_no:
            if hasattr(self.icp_no, 'to_alipay_dict'):
                params['icp_no'] = self.icp_no.to_alipay_dict()
            else:
                params['icp_no'] = self.icp_no
        if self.icp_org_name:
            if hasattr(self.icp_org_name, 'to_alipay_dict'):
                params['icp_org_name'] = self.icp_org_name.to_alipay_dict()
            else:
                params['icp_org_name'] = self.icp_org_name
        if self.icp_service_name:
            if hasattr(self.icp_service_name, 'to_alipay_dict'):
                params['icp_service_name'] = self.icp_service_name.to_alipay_dict()
            else:
                params['icp_service_name'] = self.icp_service_name
        if self.market:
            if hasattr(self.market, 'to_alipay_dict'):
                params['market'] = self.market.to_alipay_dict()
            else:
                params['market'] = self.market
        if self.password:
            if hasattr(self.password, 'to_alipay_dict'):
                params['password'] = self.password.to_alipay_dict()
            else:
                params['password'] = self.password
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.remark_image:
            if hasattr(self.remark_image, 'to_alipay_dict'):
                params['remark_image'] = self.remark_image.to_alipay_dict()
            else:
                params['remark_image'] = self.remark_image
        if self.screenshot_image:
            if hasattr(self.screenshot_image, 'to_alipay_dict'):
                params['screenshot_image'] = self.screenshot_image.to_alipay_dict()
            else:
                params['screenshot_image'] = self.screenshot_image
        if self.site_domain:
            if hasattr(self.site_domain, 'to_alipay_dict'):
                params['site_domain'] = self.site_domain.to_alipay_dict()
            else:
                params['site_domain'] = self.site_domain
        if self.site_name:
            if hasattr(self.site_name, 'to_alipay_dict'):
                params['site_name'] = self.site_name.to_alipay_dict()
            else:
                params['site_name'] = self.site_name
        if self.site_type:
            if hasattr(self.site_type, 'to_alipay_dict'):
                params['site_type'] = self.site_type.to_alipay_dict()
            else:
                params['site_type'] = self.site_type
        if self.site_url:
            if hasattr(self.site_url, 'to_alipay_dict'):
                params['site_url'] = self.site_url.to_alipay_dict()
            else:
                params['site_url'] = self.site_url
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tiny_app_id:
            if hasattr(self.tiny_app_id, 'to_alipay_dict'):
                params['tiny_app_id'] = self.tiny_app_id.to_alipay_dict()
            else:
                params['tiny_app_id'] = self.tiny_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SiteInfo()
        if 'account' in d:
            o.account = d['account']
        if 'auth_letter_image' in d:
            o.auth_letter_image = d['auth_letter_image']
        if 'download' in d:
            o.download = d['download']
        if 'icp_no' in d:
            o.icp_no = d['icp_no']
        if 'icp_org_name' in d:
            o.icp_org_name = d['icp_org_name']
        if 'icp_service_name' in d:
            o.icp_service_name = d['icp_service_name']
        if 'market' in d:
            o.market = d['market']
        if 'password' in d:
            o.password = d['password']
        if 'remark' in d:
            o.remark = d['remark']
        if 'remark_image' in d:
            o.remark_image = d['remark_image']
        if 'screenshot_image' in d:
            o.screenshot_image = d['screenshot_image']
        if 'site_domain' in d:
            o.site_domain = d['site_domain']
        if 'site_name' in d:
            o.site_name = d['site_name']
        if 'site_type' in d:
            o.site_type = d['site_type']
        if 'site_url' in d:
            o.site_url = d['site_url']
        if 'status' in d:
            o.status = d['status']
        if 'tiny_app_id' in d:
            o.tiny_app_id = d['tiny_app_id']
        return o


