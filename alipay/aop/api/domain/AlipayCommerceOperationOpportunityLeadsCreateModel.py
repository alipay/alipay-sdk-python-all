#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BizEntityInfo import BizEntityInfo
from alipay.aop.api.domain.BsCashierInfo import BsCashierInfo
from alipay.aop.api.domain.BsCertificateInfo import BsCertificateInfo
from alipay.aop.api.domain.BsContactPersonInfo import BsContactPersonInfo
from alipay.aop.api.domain.BsExtraCredentials import BsExtraCredentials
from alipay.aop.api.domain.BsMccInfo import BsMccInfo
from alipay.aop.api.domain.BsShopInfoDetail import BsShopInfoDetail


class AlipayCommerceOperationOpportunityLeadsCreateModel(object):

    def __init__(self):
        self._biz_entity_info = None
        self._cashier_info = None
        self._certificate_info = None
        self._contact_person_info = None
        self._custom_pricing = None
        self._device_num = None
        self._device_type = None
        self._extra_credentials = None
        self._leads_from = None
        self._mcc_info = None
        self._opportunity_id = None
        self._out_biz_no = None
        self._out_trade_no = None
        self._shop_info = None
        self._source = None

    @property
    def biz_entity_info(self):
        return self._biz_entity_info

    @biz_entity_info.setter
    def biz_entity_info(self, value):
        if isinstance(value, BizEntityInfo):
            self._biz_entity_info = value
        else:
            self._biz_entity_info = BizEntityInfo.from_alipay_dict(value)
    @property
    def cashier_info(self):
        return self._cashier_info

    @cashier_info.setter
    def cashier_info(self, value):
        if isinstance(value, list):
            self._cashier_info = list()
            for i in value:
                if isinstance(i, BsCashierInfo):
                    self._cashier_info.append(i)
                else:
                    self._cashier_info.append(BsCashierInfo.from_alipay_dict(i))
    @property
    def certificate_info(self):
        return self._certificate_info

    @certificate_info.setter
    def certificate_info(self, value):
        if isinstance(value, BsCertificateInfo):
            self._certificate_info = value
        else:
            self._certificate_info = BsCertificateInfo.from_alipay_dict(value)
    @property
    def contact_person_info(self):
        return self._contact_person_info

    @contact_person_info.setter
    def contact_person_info(self, value):
        if isinstance(value, BsContactPersonInfo):
            self._contact_person_info = value
        else:
            self._contact_person_info = BsContactPersonInfo.from_alipay_dict(value)
    @property
    def custom_pricing(self):
        return self._custom_pricing

    @custom_pricing.setter
    def custom_pricing(self, value):
        self._custom_pricing = value
    @property
    def device_num(self):
        return self._device_num

    @device_num.setter
    def device_num(self, value):
        self._device_num = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def extra_credentials(self):
        return self._extra_credentials

    @extra_credentials.setter
    def extra_credentials(self, value):
        if isinstance(value, BsExtraCredentials):
            self._extra_credentials = value
        else:
            self._extra_credentials = BsExtraCredentials.from_alipay_dict(value)
    @property
    def leads_from(self):
        return self._leads_from

    @leads_from.setter
    def leads_from(self, value):
        self._leads_from = value
    @property
    def mcc_info(self):
        return self._mcc_info

    @mcc_info.setter
    def mcc_info(self, value):
        if isinstance(value, BsMccInfo):
            self._mcc_info = value
        else:
            self._mcc_info = BsMccInfo.from_alipay_dict(value)
    @property
    def opportunity_id(self):
        return self._opportunity_id

    @opportunity_id.setter
    def opportunity_id(self, value):
        self._opportunity_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def shop_info(self):
        return self._shop_info

    @shop_info.setter
    def shop_info(self, value):
        if isinstance(value, BsShopInfoDetail):
            self._shop_info = value
        else:
            self._shop_info = BsShopInfoDetail.from_alipay_dict(value)
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_entity_info:
            if hasattr(self.biz_entity_info, 'to_alipay_dict'):
                params['biz_entity_info'] = self.biz_entity_info.to_alipay_dict()
            else:
                params['biz_entity_info'] = self.biz_entity_info
        if self.cashier_info:
            if isinstance(self.cashier_info, list):
                for i in range(0, len(self.cashier_info)):
                    element = self.cashier_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cashier_info[i] = element.to_alipay_dict()
            if hasattr(self.cashier_info, 'to_alipay_dict'):
                params['cashier_info'] = self.cashier_info.to_alipay_dict()
            else:
                params['cashier_info'] = self.cashier_info
        if self.certificate_info:
            if hasattr(self.certificate_info, 'to_alipay_dict'):
                params['certificate_info'] = self.certificate_info.to_alipay_dict()
            else:
                params['certificate_info'] = self.certificate_info
        if self.contact_person_info:
            if hasattr(self.contact_person_info, 'to_alipay_dict'):
                params['contact_person_info'] = self.contact_person_info.to_alipay_dict()
            else:
                params['contact_person_info'] = self.contact_person_info
        if self.custom_pricing:
            if hasattr(self.custom_pricing, 'to_alipay_dict'):
                params['custom_pricing'] = self.custom_pricing.to_alipay_dict()
            else:
                params['custom_pricing'] = self.custom_pricing
        if self.device_num:
            if hasattr(self.device_num, 'to_alipay_dict'):
                params['device_num'] = self.device_num.to_alipay_dict()
            else:
                params['device_num'] = self.device_num
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.extra_credentials:
            if hasattr(self.extra_credentials, 'to_alipay_dict'):
                params['extra_credentials'] = self.extra_credentials.to_alipay_dict()
            else:
                params['extra_credentials'] = self.extra_credentials
        if self.leads_from:
            if hasattr(self.leads_from, 'to_alipay_dict'):
                params['leads_from'] = self.leads_from.to_alipay_dict()
            else:
                params['leads_from'] = self.leads_from
        if self.mcc_info:
            if hasattr(self.mcc_info, 'to_alipay_dict'):
                params['mcc_info'] = self.mcc_info.to_alipay_dict()
            else:
                params['mcc_info'] = self.mcc_info
        if self.opportunity_id:
            if hasattr(self.opportunity_id, 'to_alipay_dict'):
                params['opportunity_id'] = self.opportunity_id.to_alipay_dict()
            else:
                params['opportunity_id'] = self.opportunity_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.shop_info:
            if hasattr(self.shop_info, 'to_alipay_dict'):
                params['shop_info'] = self.shop_info.to_alipay_dict()
            else:
                params['shop_info'] = self.shop_info
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationOpportunityLeadsCreateModel()
        if 'biz_entity_info' in d:
            o.biz_entity_info = d['biz_entity_info']
        if 'cashier_info' in d:
            o.cashier_info = d['cashier_info']
        if 'certificate_info' in d:
            o.certificate_info = d['certificate_info']
        if 'contact_person_info' in d:
            o.contact_person_info = d['contact_person_info']
        if 'custom_pricing' in d:
            o.custom_pricing = d['custom_pricing']
        if 'device_num' in d:
            o.device_num = d['device_num']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'extra_credentials' in d:
            o.extra_credentials = d['extra_credentials']
        if 'leads_from' in d:
            o.leads_from = d['leads_from']
        if 'mcc_info' in d:
            o.mcc_info = d['mcc_info']
        if 'opportunity_id' in d:
            o.opportunity_id = d['opportunity_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'shop_info' in d:
            o.shop_info = d['shop_info']
        if 'source' in d:
            o.source = d['source']
        return o


