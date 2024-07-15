#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentCustomerDetail import RentCustomerDetail
from alipay.aop.api.domain.RentDeliveryDetail import RentDeliveryDetail
from alipay.aop.api.domain.RentItemDetail import RentItemDetail
from alipay.aop.api.domain.RentManualRiskDetail import RentManualRiskDetail
from alipay.aop.api.domain.OverdueDetail import OverdueDetail
from alipay.aop.api.domain.AutoRentPhaseRiskDetail import AutoRentPhaseRiskDetail
from alipay.aop.api.domain.RentPriceDetail import RentPriceDetail


class AlipayCloudTraasMpcmrchOrderModifyModel(object):

    def __init__(self):
        self._customer_detail = None
        self._customer_id = None
        self._customer_type = None
        self._delivery_detail = None
        self._item_detail = None
        self._manual_risk_detail = None
        self._order_create_time = None
        self._out_biz_no = None
        self._overdue_detail = None
        self._phase_risk_details = None
        self._price_detail = None
        self._source = None
        self._status = None

    @property
    def customer_detail(self):
        return self._customer_detail

    @customer_detail.setter
    def customer_detail(self, value):
        if isinstance(value, RentCustomerDetail):
            self._customer_detail = value
        else:
            self._customer_detail = RentCustomerDetail.from_alipay_dict(value)
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def customer_type(self):
        return self._customer_type

    @customer_type.setter
    def customer_type(self, value):
        self._customer_type = value
    @property
    def delivery_detail(self):
        return self._delivery_detail

    @delivery_detail.setter
    def delivery_detail(self, value):
        if isinstance(value, RentDeliveryDetail):
            self._delivery_detail = value
        else:
            self._delivery_detail = RentDeliveryDetail.from_alipay_dict(value)
    @property
    def item_detail(self):
        return self._item_detail

    @item_detail.setter
    def item_detail(self, value):
        if isinstance(value, RentItemDetail):
            self._item_detail = value
        else:
            self._item_detail = RentItemDetail.from_alipay_dict(value)
    @property
    def manual_risk_detail(self):
        return self._manual_risk_detail

    @manual_risk_detail.setter
    def manual_risk_detail(self, value):
        if isinstance(value, RentManualRiskDetail):
            self._manual_risk_detail = value
        else:
            self._manual_risk_detail = RentManualRiskDetail.from_alipay_dict(value)
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def overdue_detail(self):
        return self._overdue_detail

    @overdue_detail.setter
    def overdue_detail(self, value):
        if isinstance(value, OverdueDetail):
            self._overdue_detail = value
        else:
            self._overdue_detail = OverdueDetail.from_alipay_dict(value)
    @property
    def phase_risk_details(self):
        return self._phase_risk_details

    @phase_risk_details.setter
    def phase_risk_details(self, value):
        if isinstance(value, list):
            self._phase_risk_details = list()
            for i in value:
                if isinstance(i, AutoRentPhaseRiskDetail):
                    self._phase_risk_details.append(i)
                else:
                    self._phase_risk_details.append(AutoRentPhaseRiskDetail.from_alipay_dict(i))
    @property
    def price_detail(self):
        return self._price_detail

    @price_detail.setter
    def price_detail(self, value):
        if isinstance(value, RentPriceDetail):
            self._price_detail = value
        else:
            self._price_detail = RentPriceDetail.from_alipay_dict(value)
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_detail:
            if hasattr(self.customer_detail, 'to_alipay_dict'):
                params['customer_detail'] = self.customer_detail.to_alipay_dict()
            else:
                params['customer_detail'] = self.customer_detail
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.customer_type:
            if hasattr(self.customer_type, 'to_alipay_dict'):
                params['customer_type'] = self.customer_type.to_alipay_dict()
            else:
                params['customer_type'] = self.customer_type
        if self.delivery_detail:
            if hasattr(self.delivery_detail, 'to_alipay_dict'):
                params['delivery_detail'] = self.delivery_detail.to_alipay_dict()
            else:
                params['delivery_detail'] = self.delivery_detail
        if self.item_detail:
            if hasattr(self.item_detail, 'to_alipay_dict'):
                params['item_detail'] = self.item_detail.to_alipay_dict()
            else:
                params['item_detail'] = self.item_detail
        if self.manual_risk_detail:
            if hasattr(self.manual_risk_detail, 'to_alipay_dict'):
                params['manual_risk_detail'] = self.manual_risk_detail.to_alipay_dict()
            else:
                params['manual_risk_detail'] = self.manual_risk_detail
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.overdue_detail:
            if hasattr(self.overdue_detail, 'to_alipay_dict'):
                params['overdue_detail'] = self.overdue_detail.to_alipay_dict()
            else:
                params['overdue_detail'] = self.overdue_detail
        if self.phase_risk_details:
            if isinstance(self.phase_risk_details, list):
                for i in range(0, len(self.phase_risk_details)):
                    element = self.phase_risk_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.phase_risk_details[i] = element.to_alipay_dict()
            if hasattr(self.phase_risk_details, 'to_alipay_dict'):
                params['phase_risk_details'] = self.phase_risk_details.to_alipay_dict()
            else:
                params['phase_risk_details'] = self.phase_risk_details
        if self.price_detail:
            if hasattr(self.price_detail, 'to_alipay_dict'):
                params['price_detail'] = self.price_detail.to_alipay_dict()
            else:
                params['price_detail'] = self.price_detail
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudTraasMpcmrchOrderModifyModel()
        if 'customer_detail' in d:
            o.customer_detail = d['customer_detail']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'customer_type' in d:
            o.customer_type = d['customer_type']
        if 'delivery_detail' in d:
            o.delivery_detail = d['delivery_detail']
        if 'item_detail' in d:
            o.item_detail = d['item_detail']
        if 'manual_risk_detail' in d:
            o.manual_risk_detail = d['manual_risk_detail']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'overdue_detail' in d:
            o.overdue_detail = d['overdue_detail']
        if 'phase_risk_details' in d:
            o.phase_risk_details = d['phase_risk_details']
        if 'price_detail' in d:
            o.price_detail = d['price_detail']
        if 'source' in d:
            o.source = d['source']
        if 'status' in d:
            o.status = d['status']
        return o


