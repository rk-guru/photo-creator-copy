import os

from pydantic import BaseModel, Field

from autotrain.trainers.common import AutoTrainParams


class ImageClassificationParams(AutoTrainParams):
    data_path: str = Field(None, title="Data path")
    model: str = Field("google/vit-base-patch16-224", title="Model name")
    lr: float = Field(5e-5, title="Learning rate")
    epochs: int = Field(3, title="Number of training epochs")
    batch_size: int = Field(8, title="Training batch size")
    warmup_ratio: float = Field(0.1, title="Warmup proportion")
    gradient_accumulation: int = Field(1, title="Gradient accumulation steps")
    optimizer: str = Field("adamw_torch", title="Optimizer")
    scheduler: str = Field("linear", title="Scheduler")
    weight_decay: float = Field(0.0, title="Weight decay")
    max_grad_norm: float = Field(1.0, title="Max gradient norm")
    seed: int = Field(42, title="Seed")
    train_split: str = Field("train", title="Train split")
    valid_split: str = Field(None, title="Validation split")
    logging_steps: int = Field(-1, title="Logging steps")
    project_name: str = Field("Project Name", title="Output directory")
    auto_find_batch_size: bool = Field(False, title="Auto find batch size")
    fp16: bool = Field(False, title="Enable fp16")
    save_total_limit: int = Field(1, title="Save total limit")
    save_strategy: str = Field("epoch", title="Save strategy")
    token: str = Field(None, title="Hub Token")
    push_to_hub: bool = Field(False, title="Push to hub")
    repo_id: str = Field(None, title="Repo id")
    evaluation_strategy: str = Field("epoch", title="Evaluation strategy")
    image_column: str = Field("image", title="Image column")
    target_column: str = Field("target", title="Target column")
    log: str = Field("none", title="Logging using experiment tracking")
