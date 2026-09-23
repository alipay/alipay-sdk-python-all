#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoyagerVoucherInfo import VoyagerVoucherInfo


class VoyagerCampaignInfo(object):

    def __init__(self):
        self._available = None
        self._btn_text = None
        self._btn_url = None
        self._campaign_id = None
        self._campaign_status = None
        self._desc = None
        self._extend_info = None
        self._logo_url = None
        self._sub_title = None
        self._title = None
        self._voucher_infos = None

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value
    @property
    def btn_text(self):
        return self._btn_text

    @btn_text.setter
    def btn_text(self, value):
        self._btn_text = value
    @property
    def btn_url(self):
        return self._btn_url

    @btn_url.setter
    def btn_url(self, value):
        self._btn_url = value
    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        self._campaign_id = value
    @property
    def campaign_status(self):
        return self._campaign_status

    @campaign_status.setter
    def campaign_status(self, value):
        self._campaign_status = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def voucher_infos(self):
        return self._voucher_infos

    @voucher_infos.setter
    def voucher_infos(self, value):
        if isinstance(value, list):
            self._voucher_infos = list()
            for i in value:
                if isinstance(i, VoyagerVoucherInfo):
                    self._voucher_infos.append(i)
                else:
                    self._voucher_infos.append(VoyagerVoucherInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.available:
            if hasattr(self.available, 'to_alipay_dict'):
                params['available'] = self.available.to_alipay_dict()
            else:
                params['available'] = self.available
        if self.btn_text:
            if hasattr(self.btn_text, 'to_alipay_dict'):
                params['btn_text'] = self.btn_text.to_alipay_dict()
            else:
                params['btn_text'] = self.btn_text
        if self.btn_url:
            if hasattr(self.btn_url, 'to_alipay_dict'):
                params['btn_url'] = self.btn_url.to_alipay_dict()
            else:
                params['btn_url'] = self.btn_url
        if self.campaign_id:
            if hasattr(self.campaign_id, 'to_alipay_dict'):
                params['campaign_id'] = self.campaign_id.to_alipay_dict()
            else:
                params['campaign_id'] = self.campaign_id
        if self.campaign_status:
            if hasattr(self.campaign_status, 'to_alipay_dict'):
                params['campaign_status'] = self.campaign_status.to_alipay_dict()
            else:
                params['campaign_status'] = self.campaign_status
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.voucher_infos:
            if isinstance(self.voucher_infos, list):
                for i in range(0, len(self.voucher_infos)):
                    element = self.voucher_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_infos[i] = element.to_alipay_dict()
            if hasattr(self.voucher_infos, 'to_alipay_dict'):
                params['voucher_infos'] = self.voucher_infos.to_alipay_dict()
            else:
                params['voucher_infos'] = self.voucher_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoyagerCampaignInfo()
        if 'available' in d:
            o.available = d['available']
        if 'btn_text' in d:
            o.btn_text = d['btn_text']
        if 'btn_url' in d:
            o.btn_url = d['btn_url']
        if 'campaign_id' in d:
            o.campaign_id = d['campaign_id']
        if 'campaign_status' in d:
            o.campaign_status = d['campaign_status']
        if 'desc' in d:
            o.desc = d['desc']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'title' in d:
            o.title = d['title']
        if 'voucher_infos' in d:
            o.voucher_infos = d['voucher_infos']
        return o


