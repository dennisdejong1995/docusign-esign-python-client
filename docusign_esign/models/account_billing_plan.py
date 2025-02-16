# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class AccountBillingPlan(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'add_ons': 'list[AddOn]',
        'app_store_receipt_expiration_date': 'str',
        'app_store_receipt_purchase_date': 'str',
        'can_cancel_renewal': 'str',
        'can_upgrade': 'str',
        'currency_code': 'str',
        'downgrade_plan_information': 'DowngradePlanUpdateResponse',
        'enable_support': 'str',
        'included_seats': 'str',
        'incremental_seats': 'str',
        'is_downgrade': 'str',
        'notification_type': 'str',
        'other_discount_percent': 'str',
        'payment_cycle': 'str',
        'payment_method': 'str',
        'per_seat_price': 'str',
        'plan_classification': 'str',
        'plan_feature_sets': 'list[FeatureSet]',
        'plan_id': 'str',
        'plan_name': 'str',
        'plan_start_date': 'str',
        'renewal_date': 'str',
        'renewal_status': 'str',
        'seat_discounts': 'list[SeatDiscount]',
        'subscription_start_date': 'str',
        'support_incident_fee': 'str',
        'support_plan_fee': 'str'
    }

    attribute_map = {
        'add_ons': 'addOns',
        'app_store_receipt_expiration_date': 'appStoreReceiptExpirationDate',
        'app_store_receipt_purchase_date': 'appStoreReceiptPurchaseDate',
        'can_cancel_renewal': 'canCancelRenewal',
        'can_upgrade': 'canUpgrade',
        'currency_code': 'currencyCode',
        'downgrade_plan_information': 'downgradePlanInformation',
        'enable_support': 'enableSupport',
        'included_seats': 'includedSeats',
        'incremental_seats': 'incrementalSeats',
        'is_downgrade': 'isDowngrade',
        'notification_type': 'notificationType',
        'other_discount_percent': 'otherDiscountPercent',
        'payment_cycle': 'paymentCycle',
        'payment_method': 'paymentMethod',
        'per_seat_price': 'perSeatPrice',
        'plan_classification': 'planClassification',
        'plan_feature_sets': 'planFeatureSets',
        'plan_id': 'planId',
        'plan_name': 'planName',
        'plan_start_date': 'planStartDate',
        'renewal_date': 'renewalDate',
        'renewal_status': 'renewalStatus',
        'seat_discounts': 'seatDiscounts',
        'subscription_start_date': 'subscriptionStartDate',
        'support_incident_fee': 'supportIncidentFee',
        'support_plan_fee': 'supportPlanFee'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """AccountBillingPlan - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._add_ons = None
        self._app_store_receipt_expiration_date = None
        self._app_store_receipt_purchase_date = None
        self._can_cancel_renewal = None
        self._can_upgrade = None
        self._currency_code = None
        self._downgrade_plan_information = None
        self._enable_support = None
        self._included_seats = None
        self._incremental_seats = None
        self._is_downgrade = None
        self._notification_type = None
        self._other_discount_percent = None
        self._payment_cycle = None
        self._payment_method = None
        self._per_seat_price = None
        self._plan_classification = None
        self._plan_feature_sets = None
        self._plan_id = None
        self._plan_name = None
        self._plan_start_date = None
        self._renewal_date = None
        self._renewal_status = None
        self._seat_discounts = None
        self._subscription_start_date = None
        self._support_incident_fee = None
        self._support_plan_fee = None
        self.discriminator = None

        setattr(self, "_{}".format('add_ons'), kwargs.get('add_ons', None))
        setattr(self, "_{}".format('app_store_receipt_expiration_date'), kwargs.get('app_store_receipt_expiration_date', None))
        setattr(self, "_{}".format('app_store_receipt_purchase_date'), kwargs.get('app_store_receipt_purchase_date', None))
        setattr(self, "_{}".format('can_cancel_renewal'), kwargs.get('can_cancel_renewal', None))
        setattr(self, "_{}".format('can_upgrade'), kwargs.get('can_upgrade', None))
        setattr(self, "_{}".format('currency_code'), kwargs.get('currency_code', None))
        setattr(self, "_{}".format('downgrade_plan_information'), kwargs.get('downgrade_plan_information', None))
        setattr(self, "_{}".format('enable_support'), kwargs.get('enable_support', None))
        setattr(self, "_{}".format('included_seats'), kwargs.get('included_seats', None))
        setattr(self, "_{}".format('incremental_seats'), kwargs.get('incremental_seats', None))
        setattr(self, "_{}".format('is_downgrade'), kwargs.get('is_downgrade', None))
        setattr(self, "_{}".format('notification_type'), kwargs.get('notification_type', None))
        setattr(self, "_{}".format('other_discount_percent'), kwargs.get('other_discount_percent', None))
        setattr(self, "_{}".format('payment_cycle'), kwargs.get('payment_cycle', None))
        setattr(self, "_{}".format('payment_method'), kwargs.get('payment_method', None))
        setattr(self, "_{}".format('per_seat_price'), kwargs.get('per_seat_price', None))
        setattr(self, "_{}".format('plan_classification'), kwargs.get('plan_classification', None))
        setattr(self, "_{}".format('plan_feature_sets'), kwargs.get('plan_feature_sets', None))
        setattr(self, "_{}".format('plan_id'), kwargs.get('plan_id', None))
        setattr(self, "_{}".format('plan_name'), kwargs.get('plan_name', None))
        setattr(self, "_{}".format('plan_start_date'), kwargs.get('plan_start_date', None))
        setattr(self, "_{}".format('renewal_date'), kwargs.get('renewal_date', None))
        setattr(self, "_{}".format('renewal_status'), kwargs.get('renewal_status', None))
        setattr(self, "_{}".format('seat_discounts'), kwargs.get('seat_discounts', None))
        setattr(self, "_{}".format('subscription_start_date'), kwargs.get('subscription_start_date', None))
        setattr(self, "_{}".format('support_incident_fee'), kwargs.get('support_incident_fee', None))
        setattr(self, "_{}".format('support_plan_fee'), kwargs.get('support_plan_fee', None))

    @property
    def add_ons(self):
        """Gets the add_ons of this AccountBillingPlan.  # noqa: E501

        Reserved:  # noqa: E501

        :return: The add_ons of this AccountBillingPlan.  # noqa: E501
        :rtype: list[AddOn]
        """
        return self._add_ons

    @add_ons.setter
    def add_ons(self, add_ons):
        """Sets the add_ons of this AccountBillingPlan.

        Reserved:  # noqa: E501

        :param add_ons: The add_ons of this AccountBillingPlan.  # noqa: E501
        :type: list[AddOn]
        """

        self._add_ons = add_ons

    @property
    def app_store_receipt_expiration_date(self):
        """Gets the app_store_receipt_expiration_date of this AccountBillingPlan.  # noqa: E501

          # noqa: E501

        :return: The app_store_receipt_expiration_date of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._app_store_receipt_expiration_date

    @app_store_receipt_expiration_date.setter
    def app_store_receipt_expiration_date(self, app_store_receipt_expiration_date):
        """Sets the app_store_receipt_expiration_date of this AccountBillingPlan.

          # noqa: E501

        :param app_store_receipt_expiration_date: The app_store_receipt_expiration_date of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._app_store_receipt_expiration_date = app_store_receipt_expiration_date

    @property
    def app_store_receipt_purchase_date(self):
        """Gets the app_store_receipt_purchase_date of this AccountBillingPlan.  # noqa: E501

          # noqa: E501

        :return: The app_store_receipt_purchase_date of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._app_store_receipt_purchase_date

    @app_store_receipt_purchase_date.setter
    def app_store_receipt_purchase_date(self, app_store_receipt_purchase_date):
        """Sets the app_store_receipt_purchase_date of this AccountBillingPlan.

          # noqa: E501

        :param app_store_receipt_purchase_date: The app_store_receipt_purchase_date of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._app_store_receipt_purchase_date = app_store_receipt_purchase_date

    @property
    def can_cancel_renewal(self):
        """Gets the can_cancel_renewal of this AccountBillingPlan.  # noqa: E501

        Reserved: TBD  # noqa: E501

        :return: The can_cancel_renewal of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._can_cancel_renewal

    @can_cancel_renewal.setter
    def can_cancel_renewal(self, can_cancel_renewal):
        """Sets the can_cancel_renewal of this AccountBillingPlan.

        Reserved: TBD  # noqa: E501

        :param can_cancel_renewal: The can_cancel_renewal of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._can_cancel_renewal = can_cancel_renewal

    @property
    def can_upgrade(self):
        """Gets the can_upgrade of this AccountBillingPlan.  # noqa: E501

        When set to **true**, specifies that you can upgrade the account through the API.  # noqa: E501

        :return: The can_upgrade of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._can_upgrade

    @can_upgrade.setter
    def can_upgrade(self, can_upgrade):
        """Sets the can_upgrade of this AccountBillingPlan.

        When set to **true**, specifies that you can upgrade the account through the API.  # noqa: E501

        :param can_upgrade: The can_upgrade of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._can_upgrade = can_upgrade

    @property
    def currency_code(self):
        """Gets the currency_code of this AccountBillingPlan.  # noqa: E501

        Specifies the ISO currency code for the account.  # noqa: E501

        :return: The currency_code of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this AccountBillingPlan.

        Specifies the ISO currency code for the account.  # noqa: E501

        :param currency_code: The currency_code of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def downgrade_plan_information(self):
        """Gets the downgrade_plan_information of this AccountBillingPlan.  # noqa: E501


        :return: The downgrade_plan_information of this AccountBillingPlan.  # noqa: E501
        :rtype: DowngradePlanUpdateResponse
        """
        return self._downgrade_plan_information

    @downgrade_plan_information.setter
    def downgrade_plan_information(self, downgrade_plan_information):
        """Sets the downgrade_plan_information of this AccountBillingPlan.


        :param downgrade_plan_information: The downgrade_plan_information of this AccountBillingPlan.  # noqa: E501
        :type: DowngradePlanUpdateResponse
        """

        self._downgrade_plan_information = downgrade_plan_information

    @property
    def enable_support(self):
        """Gets the enable_support of this AccountBillingPlan.  # noqa: E501

        When set to **true**, then customer support is provided as part of the account plan.  # noqa: E501

        :return: The enable_support of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._enable_support

    @enable_support.setter
    def enable_support(self, enable_support):
        """Sets the enable_support of this AccountBillingPlan.

        When set to **true**, then customer support is provided as part of the account plan.  # noqa: E501

        :param enable_support: The enable_support of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._enable_support = enable_support

    @property
    def included_seats(self):
        """Gets the included_seats of this AccountBillingPlan.  # noqa: E501

        The number of seats (users) included.  # noqa: E501

        :return: The included_seats of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._included_seats

    @included_seats.setter
    def included_seats(self, included_seats):
        """Sets the included_seats of this AccountBillingPlan.

        The number of seats (users) included.  # noqa: E501

        :param included_seats: The included_seats of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._included_seats = included_seats

    @property
    def incremental_seats(self):
        """Gets the incremental_seats of this AccountBillingPlan.  # noqa: E501

        Reserved: TBD  # noqa: E501

        :return: The incremental_seats of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._incremental_seats

    @incremental_seats.setter
    def incremental_seats(self, incremental_seats):
        """Sets the incremental_seats of this AccountBillingPlan.

        Reserved: TBD  # noqa: E501

        :param incremental_seats: The incremental_seats of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._incremental_seats = incremental_seats

    @property
    def is_downgrade(self):
        """Gets the is_downgrade of this AccountBillingPlan.  # noqa: E501

          # noqa: E501

        :return: The is_downgrade of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._is_downgrade

    @is_downgrade.setter
    def is_downgrade(self, is_downgrade):
        """Sets the is_downgrade of this AccountBillingPlan.

          # noqa: E501

        :param is_downgrade: The is_downgrade of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._is_downgrade = is_downgrade

    @property
    def notification_type(self):
        """Gets the notification_type of this AccountBillingPlan.  # noqa: E501

          # noqa: E501

        :return: The notification_type of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        """Sets the notification_type of this AccountBillingPlan.

          # noqa: E501

        :param notification_type: The notification_type of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._notification_type = notification_type

    @property
    def other_discount_percent(self):
        """Gets the other_discount_percent of this AccountBillingPlan.  # noqa: E501

         Any other percentage discount for the plan.   # noqa: E501

        :return: The other_discount_percent of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._other_discount_percent

    @other_discount_percent.setter
    def other_discount_percent(self, other_discount_percent):
        """Sets the other_discount_percent of this AccountBillingPlan.

         Any other percentage discount for the plan.   # noqa: E501

        :param other_discount_percent: The other_discount_percent of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._other_discount_percent = other_discount_percent

    @property
    def payment_cycle(self):
        """Gets the payment_cycle of this AccountBillingPlan.  # noqa: E501

          # noqa: E501

        :return: The payment_cycle of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._payment_cycle

    @payment_cycle.setter
    def payment_cycle(self, payment_cycle):
        """Sets the payment_cycle of this AccountBillingPlan.

          # noqa: E501

        :param payment_cycle: The payment_cycle of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._payment_cycle = payment_cycle

    @property
    def payment_method(self):
        """Gets the payment_method of this AccountBillingPlan.  # noqa: E501

         The payment method used with the plan. The possible values are: CreditCard, PurchaseOrder, Premium, or Freemium.   # noqa: E501

        :return: The payment_method of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this AccountBillingPlan.

         The payment method used with the plan. The possible values are: CreditCard, PurchaseOrder, Premium, or Freemium.   # noqa: E501

        :param payment_method: The payment_method of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

    @property
    def per_seat_price(self):
        """Gets the per_seat_price of this AccountBillingPlan.  # noqa: E501

          # noqa: E501

        :return: The per_seat_price of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._per_seat_price

    @per_seat_price.setter
    def per_seat_price(self, per_seat_price):
        """Sets the per_seat_price of this AccountBillingPlan.

          # noqa: E501

        :param per_seat_price: The per_seat_price of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._per_seat_price = per_seat_price

    @property
    def plan_classification(self):
        """Gets the plan_classification of this AccountBillingPlan.  # noqa: E501

        Identifies the type of plan. Examples include Business, Corporate, Enterprise, Free.  # noqa: E501

        :return: The plan_classification of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._plan_classification

    @plan_classification.setter
    def plan_classification(self, plan_classification):
        """Sets the plan_classification of this AccountBillingPlan.

        Identifies the type of plan. Examples include Business, Corporate, Enterprise, Free.  # noqa: E501

        :param plan_classification: The plan_classification of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._plan_classification = plan_classification

    @property
    def plan_feature_sets(self):
        """Gets the plan_feature_sets of this AccountBillingPlan.  # noqa: E501

        A complex type that sets the feature sets for the account. It contains the following information (all string content):  * currencyFeatureSetPrices - Contains the currencyCode and currencySymbol for the alternate currency values for envelopeFee, fixedFee, seatFee that are configured for this plan feature set. * envelopeFee - An incremental envelope cost for plans with envelope overages (when isEnabled=true). * featureSetId - A unique ID for the feature set. * fixedFee - A one-time fee associated with the plan (when isEnabled=true). * isActive - Specifies whether the feature set is actively set as part of the plan. * isEnabled - Specifies whether the feature set is actively enabled as part of the plan. * name - The name of the feature set. * seatFee - An incremental seat cost for seat-based plans (when isEnabled=true).   # noqa: E501

        :return: The plan_feature_sets of this AccountBillingPlan.  # noqa: E501
        :rtype: list[FeatureSet]
        """
        return self._plan_feature_sets

    @plan_feature_sets.setter
    def plan_feature_sets(self, plan_feature_sets):
        """Sets the plan_feature_sets of this AccountBillingPlan.

        A complex type that sets the feature sets for the account. It contains the following information (all string content):  * currencyFeatureSetPrices - Contains the currencyCode and currencySymbol for the alternate currency values for envelopeFee, fixedFee, seatFee that are configured for this plan feature set. * envelopeFee - An incremental envelope cost for plans with envelope overages (when isEnabled=true). * featureSetId - A unique ID for the feature set. * fixedFee - A one-time fee associated with the plan (when isEnabled=true). * isActive - Specifies whether the feature set is actively set as part of the plan. * isEnabled - Specifies whether the feature set is actively enabled as part of the plan. * name - The name of the feature set. * seatFee - An incremental seat cost for seat-based plans (when isEnabled=true).   # noqa: E501

        :param plan_feature_sets: The plan_feature_sets of this AccountBillingPlan.  # noqa: E501
        :type: list[FeatureSet]
        """

        self._plan_feature_sets = plan_feature_sets

    @property
    def plan_id(self):
        """Gets the plan_id of this AccountBillingPlan.  # noqa: E501

          # noqa: E501

        :return: The plan_id of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this AccountBillingPlan.

          # noqa: E501

        :param plan_id: The plan_id of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._plan_id = plan_id

    @property
    def plan_name(self):
        """Gets the plan_name of this AccountBillingPlan.  # noqa: E501

        The name of the Billing Plan.  # noqa: E501

        :return: The plan_name of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this AccountBillingPlan.

        The name of the Billing Plan.  # noqa: E501

        :param plan_name: The plan_name of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._plan_name = plan_name

    @property
    def plan_start_date(self):
        """Gets the plan_start_date of this AccountBillingPlan.  # noqa: E501

          # noqa: E501

        :return: The plan_start_date of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._plan_start_date

    @plan_start_date.setter
    def plan_start_date(self, plan_start_date):
        """Sets the plan_start_date of this AccountBillingPlan.

          # noqa: E501

        :param plan_start_date: The plan_start_date of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._plan_start_date = plan_start_date

    @property
    def renewal_date(self):
        """Gets the renewal_date of this AccountBillingPlan.  # noqa: E501

          # noqa: E501

        :return: The renewal_date of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._renewal_date

    @renewal_date.setter
    def renewal_date(self, renewal_date):
        """Sets the renewal_date of this AccountBillingPlan.

          # noqa: E501

        :param renewal_date: The renewal_date of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._renewal_date = renewal_date

    @property
    def renewal_status(self):
        """Gets the renewal_status of this AccountBillingPlan.  # noqa: E501

        The renewal status for the account. The acceptable values are:  * auto: The account automatically renews. * queued_for_close: Account will be closed at the billingPeriodEndDate. * queued_for_downgrade: Account will be downgraded at the billingPeriodEndDate.  # noqa: E501

        :return: The renewal_status of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._renewal_status

    @renewal_status.setter
    def renewal_status(self, renewal_status):
        """Sets the renewal_status of this AccountBillingPlan.

        The renewal status for the account. The acceptable values are:  * auto: The account automatically renews. * queued_for_close: Account will be closed at the billingPeriodEndDate. * queued_for_downgrade: Account will be downgraded at the billingPeriodEndDate.  # noqa: E501

        :param renewal_status: The renewal_status of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._renewal_status = renewal_status

    @property
    def seat_discounts(self):
        """Gets the seat_discounts of this AccountBillingPlan.  # noqa: E501

         A complex type that contains any seat discount information.  Values are: BeginSeatCount, EndSeatCount, and SeatDiscountPercent.    # noqa: E501

        :return: The seat_discounts of this AccountBillingPlan.  # noqa: E501
        :rtype: list[SeatDiscount]
        """
        return self._seat_discounts

    @seat_discounts.setter
    def seat_discounts(self, seat_discounts):
        """Sets the seat_discounts of this AccountBillingPlan.

         A complex type that contains any seat discount information.  Values are: BeginSeatCount, EndSeatCount, and SeatDiscountPercent.    # noqa: E501

        :param seat_discounts: The seat_discounts of this AccountBillingPlan.  # noqa: E501
        :type: list[SeatDiscount]
        """

        self._seat_discounts = seat_discounts

    @property
    def subscription_start_date(self):
        """Gets the subscription_start_date of this AccountBillingPlan.  # noqa: E501

          # noqa: E501

        :return: The subscription_start_date of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._subscription_start_date

    @subscription_start_date.setter
    def subscription_start_date(self, subscription_start_date):
        """Sets the subscription_start_date of this AccountBillingPlan.

          # noqa: E501

        :param subscription_start_date: The subscription_start_date of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._subscription_start_date = subscription_start_date

    @property
    def support_incident_fee(self):
        """Gets the support_incident_fee of this AccountBillingPlan.  # noqa: E501

        The support incident fee charged for each support incident.  # noqa: E501

        :return: The support_incident_fee of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._support_incident_fee

    @support_incident_fee.setter
    def support_incident_fee(self, support_incident_fee):
        """Sets the support_incident_fee of this AccountBillingPlan.

        The support incident fee charged for each support incident.  # noqa: E501

        :param support_incident_fee: The support_incident_fee of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._support_incident_fee = support_incident_fee

    @property
    def support_plan_fee(self):
        """Gets the support_plan_fee of this AccountBillingPlan.  # noqa: E501

        The support plan fee charged for this plan.  # noqa: E501

        :return: The support_plan_fee of this AccountBillingPlan.  # noqa: E501
        :rtype: str
        """
        return self._support_plan_fee

    @support_plan_fee.setter
    def support_plan_fee(self, support_plan_fee):
        """Sets the support_plan_fee of this AccountBillingPlan.

        The support plan fee charged for this plan.  # noqa: E501

        :param support_plan_fee: The support_plan_fee of this AccountBillingPlan.  # noqa: E501
        :type: str
        """

        self._support_plan_fee = support_plan_fee

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AccountBillingPlan, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AccountBillingPlan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountBillingPlan):
            return True

        return self.to_dict() != other.to_dict()
