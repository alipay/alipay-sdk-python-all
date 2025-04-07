#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsOpenAttachmentDTO import InsOpenAttachmentDTO
from alipay.aop.api.domain.EcomBuyerDTO import EcomBuyerDTO
from alipay.aop.api.domain.EcomItemDTO import EcomItemDTO
from alipay.aop.api.domain.EcomOrderDTO import EcomOrderDTO
from alipay.aop.api.domain.EcomRefundDisputeDTO import EcomRefundDisputeDTO
from alipay.aop.api.domain.EcomLogisticsOrderDTO import EcomLogisticsOrderDTO
from alipay.aop.api.domain.EcomSellerDTO import EcomSellerDTO


class AlipayInsSceneEcommerceClaimApplyModel(object):

    def __init__(self):
        self._apply_amout = None
        self._attachments = None
        self._buyer = None
        self._claim_pay_mode = None
        self._claim_report_biz_info = None
        self._item = None
        self._order_dto = None
        self._partner_org_id = None
        self._policy_no = None
        self._policy_no_list = None
        self._refund_dispute = None
        self._refund_logistics_order = None
        self._report_operator_type = None
        self._report_out_biz_no = None
        self._seller = None
        self._source = None

    @property
    def apply_amout(self):
        return self._apply_amout

    @apply_amout.setter
    def apply_amout(self, value):
        self._apply_amout = value
    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        if isinstance(value, list):
            self._attachments = list()
            for i in value:
                if isinstance(i, InsOpenAttachmentDTO):
                    self._attachments.append(i)
                else:
                    self._attachments.append(InsOpenAttachmentDTO.from_alipay_dict(i))
    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        if isinstance(value, EcomBuyerDTO):
            self._buyer = value
        else:
            self._buyer = EcomBuyerDTO.from_alipay_dict(value)
    @property
    def claim_pay_mode(self):
        return self._claim_pay_mode

    @claim_pay_mode.setter
    def claim_pay_mode(self, value):
        self._claim_pay_mode = value
    @property
    def claim_report_biz_info(self):
        return self._claim_report_biz_info

    @claim_report_biz_info.setter
    def claim_report_biz_info(self, value):
        self._claim_report_biz_info = value
    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, value):
        if isinstance(value, EcomItemDTO):
            self._item = value
        else:
            self._item = EcomItemDTO.from_alipay_dict(value)
    @property
    def order_dto(self):
        return self._order_dto

    @order_dto.setter
    def order_dto(self, value):
        if isinstance(value, EcomOrderDTO):
            self._order_dto = value
        else:
            self._order_dto = EcomOrderDTO.from_alipay_dict(value)
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def policy_no_list(self):
        return self._policy_no_list

    @policy_no_list.setter
    def policy_no_list(self, value):
        if isinstance(value, list):
            self._policy_no_list = list()
            for i in value:
                self._policy_no_list.append(i)
    @property
    def refund_dispute(self):
        return self._refund_dispute

    @refund_dispute.setter
    def refund_dispute(self, value):
        if isinstance(value, EcomRefundDisputeDTO):
            self._refund_dispute = value
        else:
            self._refund_dispute = EcomRefundDisputeDTO.from_alipay_dict(value)
    @property
    def refund_logistics_order(self):
        return self._refund_logistics_order

    @refund_logistics_order.setter
    def refund_logistics_order(self, value):
        if isinstance(value, EcomLogisticsOrderDTO):
            self._refund_logistics_order = value
        else:
            self._refund_logistics_order = EcomLogisticsOrderDTO.from_alipay_dict(value)
    @property
    def report_operator_type(self):
        return self._report_operator_type

    @report_operator_type.setter
    def report_operator_type(self, value):
        self._report_operator_type = value
    @property
    def report_out_biz_no(self):
        return self._report_out_biz_no

    @report_out_biz_no.setter
    def report_out_biz_no(self, value):
        self._report_out_biz_no = value
    @property
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, value):
        if isinstance(value, EcomSellerDTO):
            self._seller = value
        else:
            self._seller = EcomSellerDTO.from_alipay_dict(value)
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_amout:
            if hasattr(self.apply_amout, 'to_alipay_dict'):
                params['apply_amout'] = self.apply_amout.to_alipay_dict()
            else:
                params['apply_amout'] = self.apply_amout
        if self.attachments:
            if isinstance(self.attachments, list):
                for i in range(0, len(self.attachments)):
                    element = self.attachments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachments[i] = element.to_alipay_dict()
            if hasattr(self.attachments, 'to_alipay_dict'):
                params['attachments'] = self.attachments.to_alipay_dict()
            else:
                params['attachments'] = self.attachments
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.claim_pay_mode:
            if hasattr(self.claim_pay_mode, 'to_alipay_dict'):
                params['claim_pay_mode'] = self.claim_pay_mode.to_alipay_dict()
            else:
                params['claim_pay_mode'] = self.claim_pay_mode
        if self.claim_report_biz_info:
            if hasattr(self.claim_report_biz_info, 'to_alipay_dict'):
                params['claim_report_biz_info'] = self.claim_report_biz_info.to_alipay_dict()
            else:
                params['claim_report_biz_info'] = self.claim_report_biz_info
        if self.item:
            if hasattr(self.item, 'to_alipay_dict'):
                params['item'] = self.item.to_alipay_dict()
            else:
                params['item'] = self.item
        if self.order_dto:
            if hasattr(self.order_dto, 'to_alipay_dict'):
                params['order_dto'] = self.order_dto.to_alipay_dict()
            else:
                params['order_dto'] = self.order_dto
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.policy_no_list:
            if isinstance(self.policy_no_list, list):
                for i in range(0, len(self.policy_no_list)):
                    element = self.policy_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.policy_no_list[i] = element.to_alipay_dict()
            if hasattr(self.policy_no_list, 'to_alipay_dict'):
                params['policy_no_list'] = self.policy_no_list.to_alipay_dict()
            else:
                params['policy_no_list'] = self.policy_no_list
        if self.refund_dispute:
            if hasattr(self.refund_dispute, 'to_alipay_dict'):
                params['refund_dispute'] = self.refund_dispute.to_alipay_dict()
            else:
                params['refund_dispute'] = self.refund_dispute
        if self.refund_logistics_order:
            if hasattr(self.refund_logistics_order, 'to_alipay_dict'):
                params['refund_logistics_order'] = self.refund_logistics_order.to_alipay_dict()
            else:
                params['refund_logistics_order'] = self.refund_logistics_order
        if self.report_operator_type:
            if hasattr(self.report_operator_type, 'to_alipay_dict'):
                params['report_operator_type'] = self.report_operator_type.to_alipay_dict()
            else:
                params['report_operator_type'] = self.report_operator_type
        if self.report_out_biz_no:
            if hasattr(self.report_out_biz_no, 'to_alipay_dict'):
                params['report_out_biz_no'] = self.report_out_biz_no.to_alipay_dict()
            else:
                params['report_out_biz_no'] = self.report_out_biz_no
        if self.seller:
            if hasattr(self.seller, 'to_alipay_dict'):
                params['seller'] = self.seller.to_alipay_dict()
            else:
                params['seller'] = self.seller
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
        o = AlipayInsSceneEcommerceClaimApplyModel()
        if 'apply_amout' in d:
            o.apply_amout = d['apply_amout']
        if 'attachments' in d:
            o.attachments = d['attachments']
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'claim_pay_mode' in d:
            o.claim_pay_mode = d['claim_pay_mode']
        if 'claim_report_biz_info' in d:
            o.claim_report_biz_info = d['claim_report_biz_info']
        if 'item' in d:
            o.item = d['item']
        if 'order_dto' in d:
            o.order_dto = d['order_dto']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'policy_no_list' in d:
            o.policy_no_list = d['policy_no_list']
        if 'refund_dispute' in d:
            o.refund_dispute = d['refund_dispute']
        if 'refund_logistics_order' in d:
            o.refund_logistics_order = d['refund_logistics_order']
        if 'report_operator_type' in d:
            o.report_operator_type = d['report_operator_type']
        if 'report_out_biz_no' in d:
            o.report_out_biz_no = d['report_out_biz_no']
        if 'seller' in d:
            o.seller = d['seller']
        if 'source' in d:
            o.source = d['source']
        return o


